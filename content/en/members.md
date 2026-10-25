---
title: "Membership management"
seo_title: "Free and open source membership management software"
slug: "membership-management"
description: "Free and open source membership management software for associations: customizable member cards, searches, groups, mailings, cards and labels, member area and online registration."
---
Keeping the members list up to date is at the heart of any association… and too often a spreadsheet going in every direction. Galette is a **free and open source membership management software**: a web application you install on your own hosting, free of charge, with no limit on the number of members, and your data stays with you.

## Member cards that fit your needs

Each member has a complete card: identity, contact information, status in the association, optional picture.

* Add your own **dynamic fields** (text, choice list, date, checkbox, file…) when the provided fields are not enough: license number, t-shirt size, medical certificate…
* Choose which fields are **mandatory**, and who can see or change them: the member themselves, the staff, administrators only.
* Attach **linked members** to a "parent" one to manage a family or the members of a same company; address and email are taken from the parent when missing.
* **Duplicate** a card to go faster, and deactivate an account rather than removing it to keep your history.

{{< img_link path="/site/assets/images/screenshots/edit_member.png" alt="Editing a member card in Galette" >}}

## Find the right member, or the right ones

The members list can be filtered and ordered in a few clicks: name, status, contribution state, group, dynamic fields. The **advanced search** combines as many criteria as needed, accepts relative dates ("certificates expiring within a month", "adult members"), and can be **saved** to run it again later.

Members can also be sorted into **groups** and sub-groups (sections, teams, committees…), each one with its managers, who only see their own groups.

{{< img_link path="/site/assets/images/screenshots/1.3.1/saved-search-dates-en.png" alt="Saved search with relative dates" >}}

## Act on a selection

Once the selection is made, everything happens from the list:

* **mailings** to members, as text or HTML, with attachments, stored to be used as templates; large mailings are split into batches to respect the limits of your mail server,
* **labels** for postal mailings, proposed right away for members without an email address,
* **member cards** and **attendance sheets** as PDF,
* **mass changes** on several cards at once,
* **CSV exports**, and **CSV imports** following a model you configure, to bring in an existing file.

## A space for every member

Every member can log in to view and **update their own card**, see their contributions, add a member of their family. Two-factor authentication is available for accounts that want it.

When you enable it, an **online registration form** lets newcomers sign up by themselves, and **public pages** display the list or the gallery of members and staff, only for those who agreed to appear there.

## What's next?

Membership management goes hand in hand with [**contributions**]({{< relref "fees.md" >}}) management: Galette computes due dates, reminds late members and generates receipts. [Plugins]({{< param "galette_doc_url" >}}/en/master/plugins/index.html) add online payment, events management, objects lending, and much more.

To go further:

* {{< doclink path="usermanual/adherents.html" >}}the members management manual{{< /doclink >}},
* {{< doclink path="usermanual/recherche.html" >}}search{{< /doclink >}} and {{< doclink path="usermanual/groups.html" >}}groups{{< /doclink >}},
* {{< doclink path="installation/index.html" >}}installation{{< /doclink >}}, or [the online demo](https://demo.galette.eu/) to try without installing anything.
