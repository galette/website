#!/usr/bin/env python3
#
# This file is part of Galette.
#
# Galette is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Galette is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Galette. If not, see https://www.gnu.org/licenses/
"""
Build data/roadmap.json for the roadmap page.

Reads the public "Galette Roadmap" project (github.com/orgs/galette/projects/5)
and, for the next maintenance release, the matching section of
galette/docs/CHANGES on its maintenance branch (1.3.4 -> 1.3.x).

Reading an organization project needs a token, even for a public project:
a fine-grained token owned by the galette organization, with the
"Projects: read-only" organization permission, in ROADMAP_TOKEN.

When anything goes wrong, the committed data/roadmap.json is kept as is and
the script exits successfully, so that the site is still built and deployed.
"""

import datetime
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ORG = "galette"
PROJECT = 5
CORE_REPO = "galette/galette"
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "roadmap.json"
MAINTENANCE_CARD = re.compile(r"^Bug fixes for (\S+)$")
# Cards closest to shipping first
STATUS_ORDER = ["Done", "In progress", "Planned", "On hold", "Idea", "Released"]

QUERY = """
query($org: String!, $number: Int!, $after: String) {
  organization(login: $org) {
    projectV2(number: $number) {
      field(name: "Version") {
        ... on ProjectV2SingleSelectField { options { name description } }
      }
      items(first: 100, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          isArchived
          content {
            ... on DraftIssue { title body }
            ... on Issue { title body }
            ... on PullRequest { title body }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } }
            }
          }
        }
      }
    }
  }
}
"""


def warn(message):
    """Report a problem as a GitHub Actions warning, or on stderr"""
    print(f"::warning title=Roadmap::{message}", file=sys.stderr)


def http(url, data=None, token=None):
    """GET or POST an URL, return the body as text"""
    headers = {"User-Agent": "galette-website-build"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if data is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(data).encode()
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=30) as response:
        return response.read().decode()


def fetch_project(token):
    """Version options and items of the roadmap project"""
    options, items, after = None, [], None
    while True:
        answer = json.loads(http(
            "https://api.github.com/graphql",
            {"query": QUERY, "variables": {"org": ORG, "number": PROJECT, "after": after}},
            token,
        ))
        if answer.get("errors"):
            raise RuntimeError("; ".join(e.get("message", "?") for e in answer["errors"]))
        project = answer["data"]["organization"]["projectV2"]
        options = project["field"]["options"]
        items += project["items"]["nodes"]
        if not project["items"]["pageInfo"]["hasNextPage"]:
            return options, items
        after = project["items"]["pageInfo"]["endCursor"]


def parse_body(body):
    """First paragraph of a card, and its checklist progress"""
    summary, total, done, intro = [], 0, 0, True
    for line in (body or "").splitlines():
        task = re.match(r"^\s*[-*] \[([ xX])\] ", line)
        if task:
            total += 1
            done += task.group(1) != " "
        if not intro:
            continue
        if re.match(r"^\s*[-*] ", line) or (summary and not line.strip()):
            intro = False
        elif line.strip() and not line.startswith("#"):
            summary.append(line.strip())
    return " ".join(summary), total, done


def changes_for(version):
    """Lines of the "X -> version" section of CHANGES, on the maintenance branch"""
    branch = re.sub(r"\.\d+$", ".x", version)
    text = http(f"https://raw.githubusercontent.com/{CORE_REPO}/{branch}/galette/docs/CHANGES")
    lines, current = [], False
    for line in text.splitlines():
        if re.match(r"^\S+ -> \S+$", line.strip()):
            current = line.strip().endswith(f"-> {version}")
            continue
        if current and line.startswith("- "):
            lines.append(line[2:].strip())
    return lines


def build(token):
    options, nodes = fetch_project(token)
    items = []
    for node in nodes:
        if node["isArchived"] or not node["content"]:
            continue
        fields = {}
        for value in node["fieldValues"]["nodes"]:
            if value and value.get("field"):
                fields[value["field"]["name"]] = value.get("name", value.get("number", value.get("text")))
        summary, total, done = parse_body(node["content"]["body"])
        items.append({
            "title": node["content"]["title"],
            "version": fields.get("Version"),
            "status": fields.get("Status"),
            "area": fields.get("Area"),
            "progress": None if fields.get("Progress") is None else round(fields["Progress"]),
            "depends": fields.get("Depends on") or None,
            "summary": summary,
            "steps": total,
            "steps_done": done,
        })

    versions = []
    for option in options:
        mine = [i for i in items if i["version"] == option["name"]]
        features = sorted(
            (i for i in mine if not MAINTENANCE_CARD.match(i["title"])),
            key=lambda i: (STATUS_ORDER.index(i["status"]) if i["status"] in STATUS_ORDER else len(STATUS_ORDER), i["title"].lower()),
        )
        released = option["description"].strip().lower() == "released"
        scheduled = bool(re.match(r"^\d", option["name"]))
        progress = [i["progress"] for i in features if i["progress"] is not None]
        version = {
            "name": option["name"],
            "description": option["description"],
            "released": released,
            # A version planned with only its "Bug fixes for X" card is a maintenance release
            "maintenance": bool(mine) and not features,
            "progress": round(sum(progress) / len(progress)) if scheduled and progress and not released else None,
            "changes": [],
            "items": features,
        }
        if version["maintenance"] and not released:
            try:
                version["changes"] = changes_for(option["name"])
            except Exception as e:  # CHANGES is a nice to have, the page works without it
                warn(f"cannot read CHANGES for {option['name']}: {e}")
        versions.append(version)

    return {
        "updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
        # Released versions, latest first, then upcoming ones in the project order
        "released": [v for v in reversed(versions) if v["released"]],
        "upcoming": [v for v in versions if not v["released"]],
    }


def main():
    token = os.environ.get("ROADMAP_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        warn(f"no ROADMAP_TOKEN, {OUTPUT.name} is not updated")
        return
    try:
        data = build(token)
    except Exception as e:
        warn(f"cannot read the roadmap project, {OUTPUT.name} is not updated: {e}")
        return
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"{OUTPUT.name}: {len(data['upcoming'])} upcoming and {len(data['released'])} released versions")


if __name__ == "__main__":
    main()
