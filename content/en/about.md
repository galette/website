---
title: "About"
description: "Galette is free and open source membership management software for associations, developed since 2003: the project, its scope, its releases, who uses it and the tools behind it."
---
<p class="lead">Galette is a web application to manage the members of associations, written in PHP, relying on a <a href="https://mariadb.org">MariaDB</a> or <a href="https://postgresql.org">PostgreSQL</a> database.</p>

{{< cards >}}
{{< card icon="scale" title="Free software" meta="GPL licence" >}}
Anyone can use, study, change and redistribute it under the terms of the [GPL licence](https://www.gnu.org/licenses/quick-guide-gplv3.html).
{{< /card >}}
{{< card icon="clock" title="Since 2003" meta="Born in a Lyon LUG" >}}
More than twenty years of changes, told on the [History]({{< ref "history" >}}) page.
{{< /card >}}
{{< card icon="users" title="A community" meta="One maintainer since 2007" >}}
Johan develops and maintains Galette; outside contributions are merged regularly.
{{< /card >}}
{{< /cards >}}

The name is a French acronym for “Gestionnaire d'Adhérents en Ligne Extrêmement Tarabiscoté mais Tellement Efficace”, roughly “Extremely Sophisticated but so Efficient On-Line Membership Manager”. In French slang, “galette” also means money. Translation kills all the fun, but [the story of the name]({{< ref "history#the-name" >}}) is worth a look.

## What Galette does

From the start, Galette has focused on managing members and their membership fees. Accounting, for instance, was left out: too far from that goal, and too heavy to develop and maintain. [Why Galette?]({{< ref "why" >}}) explains this choice.

Core features aim to be generic, to suit as many associations as possible. More specific needs are covered by [plugins]({{< ref "plugins" >}}): {{< doclink path="plugins/auto.html" >}}run a car club{{< /doclink >}}, {{< doclink path="plugins/objectslend.html" >}}lend equipment{{< /doclink >}}… Have a feature idea? Suggest it on [GitHub Discussions]({{% param "galette_discussions_url" %}}), or [help build it]({{< ref "contribute" >}}).

## Releases and support

Galette has no release schedule: a version is out when it is ready. Bugfix releases come out regularly, as soon as an important issue is fixed or several fixes have piled up.

Only one major version is maintained at a time: when a new major version is out, the previous one is no longer supported. The only possible exception is a security issue found shortly after a new major release.

## They use Galette

The [list of Galette users](https://telemetry.galette.eu/reference) is published by our telemetry application. Using Galette? [Add your association](https://telemetry.galette.eu/reference?showmodal), or {{< doclink path="usermanual/generalites.html#telemetry" >}}register from Galette{{< /doclink >}} to be able to edit your information later.

## Project tools

* [source code](https://github.com/galette/galette/): [Git](https://git-scm.com/), on GitHub,
* website: [Hugo](https://gohugo.io),
* {{< doclink >}}documentation{{< /doclink >}}: [Sphinx](https://www.sphinx-doc.org), hosted by [Read the Docs](https://readthedocs.org),
* [bug tracker]({{% param "galette_tracker_url" %}}): [Redmine](https://redmine.org),
* [translations]({{% param "galette_trad_url" %}}): [Weblate](https://weblate.org),
* [mailing lists]({{< ref "contact#mailing-lists" >}}): [Mailman](https://list.org),
* [demo](https://demo.galette.eu): Galette, of course,
* Johan: self-hosted :p
