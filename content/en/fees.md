---
title: "Membership fees management"
seo_title: "Free and open source membership fees management software"
slug: "membership-fees-management"
description: "Manage your association membership fees with Galette, free and open source software: computed due dates, automatic reminders, donations, scheduled payments, receipts and invoices as PDF."
---
Who is up to date with their membership fee? Who should be reminded? How much did donations bring this year? Galette answers those questions with no spreadsheet and no mental arithmetic: each recorded contribution updates the member's **due date**, and everything else follows.

## Contributions your way

Every association has its own rules, Galette adapts to them:

* **contribution types** you define: annual fee, reduced fee, monthly or quarterly fee, with a default amount,
* **donations** and other contributions that do not extend the membership,
* a **membership period** shared by everyone (from September 1st to August 31st, for example) or a duration running from the payment,
* **offered months** at the end of the period: with two months offered, a fee paid in November is valid for the whole next year,
* members **freed of dues**, honorary members or volunteers.

## Always know who is up to date

Each member's due date is computed automatically, and the members list shows at a glance who is up to date, who is close to the due date and who is late. Every member also sees, in their own space, the remaining days or how late they are.

The contributions list can be filtered by date, type or payment type, with the total amount of what was found. The advanced search can find, for example, all members whose membership expires within a month.

{{< img_link path="/site/assets/images/screenshots/contributions_list.png" alt="Contributions list, with its filters" >}}

## Reminders that go by themselves

Galette prepares **email reminders**: one month then seven days before the due date, then one and two months after. Each reminder is written in its recipient's language, and Galette proposes to print labels for members without an email address.

You can send reminders from the dashboard, or **automate** them with a scheduled task on your server; the sending limits of your mail server are respected.

## Payments, transactions and receipts

* A **transaction** groups a single payment dispatched among several contributions: the check of a family paying three memberships and a donation, for example.
* **Scheduled payments** split a contribution into several installments.
* Each contribution can produce its **receipt** or **invoice** as PDF, from a model you customize; members find them in their own space.
* **Online payment** comes with [HelloAsso](https://galette-plugins.github.io/plugin-helloasso/) or [Stripe](https://galette-plugins.github.io/plugin-stripe/) [plugins]({{< relref "plugins.md" >}}): the contribution is recorded as soon as the payment is validated.

## What about the rest?

Contributions go hand in hand with [membership management]({{< relref "members.md" >}}). Galette is not an accounting software, but CSV exports let you bring this data into your treasurer's tool. [Why Galette?]({{< relref "why.md" >}}) explains those choices.

To go further:

* {{< doclink path="usermanual/contributions.html" >}}the contributions management manual{{< /doclink >}},
* {{< doclink path="usermanual/reference_lists.html" >}}contribution types configuration{{< /doclink >}},
* [the online demo](https://demo.galette.eu/) to try without installing anything.
