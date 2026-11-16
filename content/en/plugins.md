---
title: "Plugins"
seo_title: "Galette plugins: online payment, events, objects lending, members map"
slug: "plugins"
description: "Extend Galette, free and open source association management software, with its free plugins: HelloAsso online payment, events, activities, objects lending, members map, single sign-on."
---
<p class="lead">Galette focuses on the essentials: <a href="{{< relref "members.md" >}}">membership management</a>, <a href="{{< relref "fees.md" >}}">membership fees</a> and <a href="{{< relref "communication.md" >}}">communication</a>. Everything else comes with <strong>plugins</strong>, free and open source: you only install what you need, and the core stays simple.</p>

{{< img_link path="/site/assets/images/screenshots/1.3.2/plugins-updates-en.png" alt="The plugins page in Galette" >}}

## Online payment

{{< cards class="two-cols" >}}
{{< card icon="card" title="HelloAsso" url="https://galette-plugins.github.io/plugin-helloasso/" button="Plugin website" >}}
Membership fees and donations paid through HelloAsso, the payment platform for French associations; the contribution is recorded as soon as the payment is validated.
{{< /card >}}
{{< card icon="card" title="Stripe" url="https://galette-plugins.github.io/plugin-stripe/" button="Plugin website" >}}
The same principle with Stripe, for membership fees and donations.
{{< /card >}}
{{< /cards >}}

## Activities and events

{{< cards class="two-cols" >}}
{{< card icon="calendar" title="Events" url="https://galette-plugins.github.io/plugin-events/" button="Plugin website" >}}
Organize events and manage your members' bookings.
{{< /card >}}
{{< card icon="checklist" title="Activities" url="https://galette-plugins.github.io/plugin-activities/" button="Plugin website" >}}
Manage the association's activities and members' subscriptions to each of them.
{{< /card >}}
{{< /cards >}}

## Equipment and vehicles

{{< cards class="two-cols" >}}
{{< card icon="package" title="ObjectsLend" url="https://galette-plugins.github.io/plugin-objectslend/" button="Plugin website" >}}
Lend and rent equipment to members, keeping track of who borrowed what.
{{< /card >}}
{{< card icon="car" title="Auto" url="https://galette-plugins.github.io/plugin-auto/" button="Plugin website" >}}
For car clubs: the vehicles of each member and their history.
{{< /card >}}
{{< /cards >}}

## Members map, single sign-on and legal notices

{{< cards >}}
{{< card icon="pin" title="Maps" url="https://galette-plugins.github.io/plugin-maps/" button="Plugin website" >}}
A map of the members who agreed to appear on it, on OpenStreetMap: no API key, self-hostable.
{{< /card >}}
{{< card icon="key" title="OAuth2" url="https://galette-plugins.github.io/plugin-oauth2/" button="Plugin website" >}}
Your members log in to your other tools (Nextcloud, Flarum…) with their Galette account: access follows the membership.
{{< /card >}}
{{< card icon="file" title="LegalNotices" url="https://galette-plugins.github.io/plugin-legalnotices/" button="Plugin website" >}}
Legal notices pages, and cookies consent if you integrate external services.
{{< /card >}}
{{< /cards >}}

## Installing a plugin

{{< steps >}}
1. **Download** the plugin from its website, which also tells the compatible Galette versions.
2. **Extract it** into the `plugins` directory of your Galette installation.
3. **Enable it** from the Galette plugins page, which also creates its tables: no command line needed.
{{< /steps >}}

All the details are in the {{< doclink path="plugins/index.html" >}}plugins documentation{{< /doclink >}}. To see several plugins in action, try [the online demo](https://demo.galette.eu/).

## Who maintains plugins?

All plugins are gathered in [the galette-plugins organization](https://github.com/galette-plugins/). Some are developed by the Galette team, along with the core; the others are maintained by their authors, members of the community.

A need that is not covered? Plugins can add pages, menus, preferences and public pages: write your own and {{< doclink path="plugins/plugins-tiers.html" >}}offer it to the organization{{< /doclink >}}, or [contact us]({{< relref "contact.md" >}}) to talk about it.
