---
title: "Pourquoi Galette ?"
seo_title: "Pourquoi Galette, logiciel de gestion d'association libre et gratuit"
slug: "pourquoi-galette"
description: "Pourquoi choisir Galette pour gérer votre association : un logiciel libre et open source, gratuit, sans limite d'adhérents, dont les données restent chez vous."
---
Les solutions pour gérer une association ne manquent pas, et beaucoup sont des plateformes en ligne : abonnement mensuel, tarif qui grimpe avec le nombre d'adhérents, commission sur les paiements, données stockées chez l'éditeur. Galette fait un autre choix : c'est un **logiciel de gestion d'association libre et gratuit**, que vous installez où vous voulez.

## Libre et open source, depuis plus de vingt ans

Galette est publié sous [licence GPL](https://www.gnu.org/licenses/quick-guide-gplv3.fr.html) : chacun peut l'utiliser, l'étudier, le modifier et le redistribuer. Le [code source](https://github.com/galette/galette/) est public, les décisions se discutent ouvertement sur le [gestionnaire de tickets]({{% param "galette_tracker_url" %}}) et le [système de vote]({{% param "galette_vote_url" %}}).

Concrètement, cela veut dire qu'aucun éditeur ne peut augmenter ses tarifs, fermer le service ou changer les conditions du jour au lendemain. Né en 2003 pour les besoins d'une association lyonnaise, le projet est maintenu par le même développeur depuis 2007 et continue d'évoluer : [son histoire]({{< relref "about.md" >}}) en dit plus.

## Gratuit, sans limite

Pas d'abonnement, pas de version « premium », pas de prix par adhérent, pas de commission. Que votre association compte 15 ou 15 000 membres, Galette est gratuit, et toutes les fonctionnalités sont disponibles. Le seul coût, c'est l'hébergement, que beaucoup d'associations ont déjà pour leur site web.

## Vos données restent chez vous

Galette tourne sur votre hébergement : les données de vos adhérents ne sont ni revendues, ni exploitées à des fins publicitaires, ni retenues si vous partez. Vous savez où elles sont et qui y accède, ce qui aide à respecter vos obligations au titre du RGPD.

* Les **exports CSV** permettent de récupérer vos données à tout moment, dans un format ouvert.
* Les **droits d'accès** se règlent champ par champ : ce que voit un adhérent, un responsable de groupe ou le bureau.
* Les **pages publiques** n'affichent que les adhérents qui ont accepté d'y figurer.
* La **double authentification** protège les comptes sensibles.

## Pensé pour les associations

Galette se concentre sur ce qui fait le quotidien d'une association : la [gestion des adhérents]({{< relref "members.md" >}}), [les cotisations]({{< relref "fees.md" >}}) et leurs échéances, les relances, les mailings, les cartes et reçus en PDF. Le choix a été fait de ne pas en faire un logiciel de comptabilité, pour rester simple et bien faire ce qu'il fait.

Ce qui sort de ce périmètre passe par des {{< doclink path="plugins/index.html" >}}plugins{{< /doclink >}} : paiement en ligne, événements, prêt de matériel, gestion d'un club automobile…

Galette est traduit dans une vingtaine de langues par sa communauté, sur [Weblate]({{% param "galette_trad_url" %}}) ; chaque adhérent utilise la langue de son choix.

## Comment démarrer ?

Plusieurs façons d'utiliser Galette, selon vos moyens techniques :

* **sur votre hébergement** : un serveur web avec PHP et une base MariaDB ou PostgreSQL suffisent ; un hébergement mutualisé fait l'affaire ({{< doclink path="installation/prerequis.html" >}}voir les prérequis{{< /doclink >}}),
* **avec Docker ou YunoHost**, pour celles et ceux qui gèrent déjà leur serveur ({{< doclink path="installation/other_methods.html" >}}autres méthodes d'installation{{< /doclink >}}),
* **chez un hébergeur associatif** du collectif [CHATONS](https://www.chatons.org/search/by-service?field_software_target_id=311), qui propose Galette clé en main,
* **avec un accompagnement professionnel** : hébergement, installation, développements sur mesure ([les services proposés]({{< relref "posts/2024-07-09-galette-pro-services.md" >}})).

Le plus simple pour vous faire une idée reste [la démo en ligne](https://demo.galette.eu/). Et si vous avez des questions, [nous sommes joignables]({{< relref "contact.md" >}}) :)
