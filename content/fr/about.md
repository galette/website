---
title: "À propos"
slug: "a-propos"
description: "Galette, logiciel libre de gestion des adhérents pour les associations, développé depuis 2003 : le projet, son périmètre, ses versions, qui l'utilise et avec quels outils il est fait."
---
<p class="lead">Galette est une application web de gestion des adhérents pour les associations, écrite en PHP, qui s'appuie sur une base <a href="https://mariadb.org">MariaDB</a> ou <a href="https://postgresql.org">PostgreSQL</a>.</p>

{{< cards >}}
{{< card icon="scale" title="Libre" meta="Licence GPL" >}}
Chacun peut l'utiliser, l'étudier, le modifier et le redistribuer selon les termes de la [licence GPL](https://www.gnu.org/licenses/quick-guide-gplv3.fr.html).
{{< /card >}}
{{< card icon="clock" title="Depuis 2003" meta="Né dans un GULL lyonnais" >}}
Plus de vingt ans d'évolutions, racontées sur la page [Histoire]({{< ref "history" >}}).
{{< /card >}}
{{< card icon="users" title="Une communauté" meta="Un mainteneur depuis 2007" >}}
Johan développe et maintient Galette ; les contributions extérieures y sont intégrées régulièrement.
{{< /card >}}
{{< /cards >}}

Le nom est un acronyme : « Gestionnaire d'Adhérents en Ligne Extrêmement Tarabiscoté mais Tellement Efficace ». En argot, la « galette », c'est aussi l'argent. [L'histoire du nom]({{< ref "history#le-nom" >}}) vaut le détour.

## Ce que fait Galette

Depuis le début, Galette se concentre sur la gestion des adhérents et des cotisations. La comptabilité, par exemple, a été écartée : trop loin de cet objectif, et trop lourde à développer et à maintenir. [Pourquoi Galette ?]({{< ref "why" >}}) détaille ce choix.

Les fonctionnalités du cœur se veulent génériques, pour convenir au plus grand nombre. Les besoins plus spécifiques passent par des [plugins]({{< ref "plugins" >}}) : {{< doclink path="plugins/auto.html" >}}gérer un club automobile{{< /doclink >}}, {{< doclink path="plugins/objectslend.html" >}}prêter du matériel{{< /doclink >}}… Une idée de fonctionnalité ? Proposez-la sur les [GitHub Discussions]({{% param "galette_discussions_url" %}}), ou [contribuez]({{< ref "contribute" >}}) à son développement.

## Versions et support

Galette n'a pas de calendrier de sortie : une version sort quand elle est prête. Des versions correctives sortent régulièrement, dès qu'un problème important est corrigé ou que plusieurs corrections se sont accumulées.

Une seule version majeure est maintenue à la fois : quand une nouvelle majeure sort, la précédente n'est plus supportée. Seule exception possible, une faille de sécurité découverte peu après la sortie d'une nouvelle majeure.

## Ils utilisent Galette

La <a href="https://telemetry.galette.eu/reference" hreflang="en">liste des utilisateurs de Galette</a> est publiée par notre application de télémétrie. Vous utilisez Galette ? <a href="https://telemetry.galette.eu/reference?showmodal" hreflang="en">Ajoutez votre association</a>, ou {{< doclink path="usermanual/generalites.html#telemetry" >}}enregistrez-vous depuis Galette{{< /doclink >}} pour pouvoir modifier vos informations par la suite.

## Les outils du projet

* [code source](https://github.com/galette/galette/) : [Git](https://git-scm.com/), sur GitHub,
* site web : [Hugo](https://gohugo.io),
* {{< doclink >}}documentation{{< /doclink >}} : [Sphinx](https://www.sphinx-doc.org), hébergée chez [Read the Docs](https://readthedocs.org),
* [gestionnaire de bogues]({{% param "galette_tracker_url" %}}) : [Redmine](https://redmine.org),
* [traductions]({{% param "galette_trad_url" %}}) : [Weblate](https://weblate.org),
* [listes de diffusion]({{< ref "contact#listes-de-discussion" >}}) : [Mailman](https://list.org),
* [démo](https://demo.galette.eu) : Galette, évidemment,
* Johan : hébergé chez lui :p
