# Galette website

## Free your association management! / Libérez la gestion de votre association !

The sources of [Galette website](https://galette.eu), which is built on the top of [Hugo](https://gohugo.io/).

All contents (pages, posts, translations, and so on are licensed under the terms of the CC BY-SA 4.0 (see LICENSE.contents file)
All source code is licensed under the terms of the GLPv3 or later (see LICENSE file).

## Roadmap page

The roadmap page (`content/en/roadmap.md`, `layouts/_default/roadmap.html`) is rendered from `data/roadmap.json`, which `bin/fetch_roadmap.py` builds from the [Galette Roadmap project](https://github.com/orgs/galette/projects/5) and, for the next maintenance release, from `galette/docs/CHANGES` on its maintenance branch.

The deploy workflow refreshes it before each build, the daily one included, with the `ROADMAP_TOKEN` secret: a fine-grained token owned by the galette organization, with the read-only "Projects" organization permission. When the project cannot be read, the committed `data/roadmap.json` is used as is.

To refresh it locally: `ROADMAP_TOKEN=$(gh auth token) python3 bin/fetch_roadmap.py`.
