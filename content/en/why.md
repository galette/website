---
title: "Why Galette?"
seo_title: "Why Galette, free and open source association management software"
slug: "why-galette"
description: "Why choose Galette to manage your association: free and open source software, free of charge, with no limit on members, and your data stays with you."
---
There is no shortage of solutions to manage an association, and many of them are online platforms: monthly subscription, prices growing with the number of members, fees on payments, data stored by the vendor. Galette makes another choice: it is a **free and open source association management software**, that you install wherever you want.

## Free and open source, for more than twenty years

Galette is published under the [GPL license](https://www.gnu.org/licenses/quick-guide-gplv3.html): anyone can use, study, change and redistribute it. The [source code](https://github.com/galette/galette/) is public, decisions are discussed openly on the [bug tracker]({{% param "galette_tracker_url" %}}) and the [voting system]({{% param "galette_vote_url" %}}).

In practice, no vendor can raise prices, shut the service down or change the terms overnight. Born in 2003 for the needs of an association in Lyon, the project has been maintained by the same developer since 2007 and keeps evolving: [its history]({{< relref "about.md" >}}) tells more.

## Free of charge, with no limit

No subscription, no "premium" edition, no price per member, no fees. Whether your association has 15 or 15,000 members, Galette is free of charge, and all features are available. The only cost is hosting, which many associations already have for their website.

## Your data stays with you

Galette runs on your own hosting: your members data is not sold, not used for advertising, and not held back if you leave. You know where it is and who can access it, which helps with your GDPR obligations.

* **CSV exports** let you retrieve your data at any time, in an open format.
* **Access rights** are set field by field: what a member, a group manager or the staff can see.
* **Public pages** only display the members who agreed to appear there.
* **Two-factor authentication** protects sensitive accounts.

## Designed for associations

Galette focuses on the day-to-day life of an association: [membership management]({{< relref "members.md" >}}), [contributions]({{< relref "fees.md" >}}) and their due dates, reminders, [mailings]({{< relref "communication.md" >}}), cards and receipts as PDF. It has been chosen not to make it an accounting software, to keep it simple and good at what it does.

What goes beyond this scope comes with {{< doclink path="plugins/index.html" >}}plugins{{< /doclink >}}: online payment, events, objects lending, car club management…

Galette is translated in about twenty languages by its community, on [Weblate]({{% param "galette_trad_url" %}}); each member uses the language of their choice.

## How to start?

There are several ways to use Galette, depending on your technical means:

* **on your hosting**: a web server with PHP and a MariaDB or PostgreSQL database are enough; a shared hosting will do ({{< doclink path="installation/prerequis.html" >}}see prerequisites{{< /doclink >}}),
* **with Docker or YunoHost**, for those who already run their own server ({{< doclink path="installation/other_methods.html" >}}other installation methods{{< /doclink >}}),
* **at a non-profit hosting provider** from the [CHATONS](https://www.chatons.org/search/by-service?field_software_target_id=311) collective, which offers ready to use Galette instances,
* **with professional services**: hosting, installation, custom developments ([the offered services]({{< relref "posts/2024-07-09-galette-pro-services.md" >}})).

The easiest way to get an idea is still [the online demo](https://demo.galette.eu/). And if you have any questions, [we can be reached]({{< relref "contact.md" >}}) :)
