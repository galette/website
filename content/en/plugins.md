---
title: "Plugins"
seo_title: "Galette plugins: online payment, events, objects lending, members map"
slug: "plugins"
description: "Extend Galette, free and open source association management software, with its free plugins: HelloAsso online payment, events, activities, objects lending, members map, single sign-on."
---
Galette focuses on the essentials: [membership management]({{< relref "members.md" >}}), [membership fees]({{< relref "fees.md" >}}) and [communication]({{< relref "communication.md" >}}). What is only useful to some associations comes with **plugins**: you only install what you need, and the core stays simple.

Plugins are free and open source, just like Galette. Once copied into the `plugins` directory of your installation, they are enabled and create their tables from the Galette plugins page, with no command line.

## Online payment

* [**HelloAsso**](https://galette-plugins.github.io/plugin-helloasso/): your members pay their membership fee or make a donation through HelloAsso, the payment platform for French associations, and the contribution is recorded in Galette as soon as the payment is validated.
* [**Stripe**](https://galette-plugins.github.io/plugin-stripe/): the same principle with Stripe, for membership fees and donations.

## Activities and events

* [**Events**](https://galette-plugins.github.io/plugin-events/): organize events and manage your members bookings.
* [**Activities**](https://galette-plugins.github.io/plugin-activities/): manage the association activities and members subscriptions to each of them.

## Equipment and vehicles

* [**ObjectsLend**](https://galette-plugins.github.io/plugin-objectslend/): lend and rent equipment to members, keeping track of who borrowed what.
* [**Auto**](https://galette-plugins.github.io/plugin-auto/): for automobile clubs, the vehicles of each member and their history.

## Members map

[**Maps**](https://galette-plugins.github.io/plugin-maps/) geolocates members and displays on a map the ones who agreed to be visible. The map relies on OpenStreetMap: no API key, no registration, and everything can be self-hosted.

## Single sign-on

[**OAuth2**](https://galette-plugins.github.io/plugin-oauth2/) turns Galette into an authentication server: your members log in with their Galette account on other tools of the association, like a Nextcloud or a Flarum forum. A single password, and access follows the membership.

## Legal notices

[**LegalNotices**](https://galette-plugins.github.io/plugin-legalnotices/) adds legal notices pages, and can handle cookies consent if you integrate external services.

## Who maintains plugins?

All plugins are gathered in [the galette-plugins organization](https://github.com/galette-plugins/). Some are developed by the Galette team, along with the core; the others are maintained by their authors, members of the community. Each plugin website tells its compatibility and how to install it.

A need that is not covered? Plugins can add pages, menus, preferences and public pages: write your own and {{< doclink path="plugins/plugins-tiers.html" >}}offer it to the organization{{< /doclink >}}, or [contact us]({{< relref "contact.md" >}}) to talk about it.

To go further:

* {{< doclink path="plugins/index.html" >}}plugins documentation{{< /doclink >}},
* [Why Galette?]({{< relref "why.md" >}}),
* [the online demo](https://demo.galette.eu/), where several plugins are enabled.
