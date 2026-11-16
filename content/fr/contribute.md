---
title: "Contribuer"
slug: "contribuer"
description: "Pas besoin d'être développeur pour contribuer à Galette : tester et signaler des bogues, aider d'autres utilisateurs, en parler, traduire, documenter, développer ou faire un don."
---
<p class="lead">Galette est un logiciel libre qui vit grâce à sa communauté. Pas besoin d'être développeur pour y participer : quelques minutes suffisent souvent pour donner un vrai coup de main.</p>

{{< donate >}}

## Choisissez comment aider

{{< cards >}}
{{< card icon="bug" title="Tester" anchor="tester" meta="Quelques minutes · aucune compétence technique" url="https://bugs.galette.eu/projects/galette/" button="Signaler un bogue" >}}
Vous utilisez Galette ? Un bogue bien décrit, c'est déjà une contribution précieuse.
{{< /card >}}
{{< card icon="help" title="Aider" anchor="aider" meta="Ponctuel · connaître Galette" url="https://github.com/orgs/galette/discussions" button="Répondre aux questions" >}}
Partagez votre expérience avec celles et ceux qui découvrent Galette.
{{< /card >}}
{{< card icon="share" title="Faire connaître" anchor="faire-connaitre" meta="Quelques minutes · aucun prérequis" url="https://framapiaf.org/@galette" button="Suivre Galette" >}}
Parlez de Galette autour de vous : d'autres associations en ont sûrement besoin.
{{< /card >}}
{{< card icon="translate" title="Traduire" anchor="traduire" meta="À votre rythme · lire l'anglais" url="https://hosted.weblate.org/projects/galette/" button="Traduire sur Weblate" >}}
Galette parle une vingtaine de langues grâce à des bénévoles. Pourquoi pas la vôtre ?
{{< /card >}}
{{< card icon="write" title="Documenter" anchor="documenter" meta="À votre rythme · écrire en anglais simple" url="https://doc.galette.eu/fr/master/" button="Lire le manuel" >}}
Le manuel gagne à être écrit par celles et ceux qui utilisent Galette au quotidien.
{{< /card >}}
{{< card icon="code" title="Développer" anchor="developper" meta="Projet · PHP, JavaScript" url="https://github.com/galette" button="Voir le code" >}}
Corrigez un bogue, améliorez un plugin ou proposez une nouvelle fonctionnalité.
{{< /card >}}
{{< /cards >}}

## Tester et signaler {#tester}

Utiliser Galette, c'est déjà soutenir le projet. Si vous tombez sur un bogue, ouvrez un ticket sur le [gestionnaire de bogues]({{% param "galette_tracker_url" %}}) avec le plus de détails possible (version, étapes pour le reproduire, message d'erreur) : c'est ce qui permet de le corriger vite. Vérifiez d'abord que personne ne l'a signalé avant vous.

Envie d'aller plus loin ? Essayez la [version nightly]({{% param "galette_nightly_url" %}}), qui contient les nouveautés en cours de développement, ou les {{< doclink path="plugins/" >}}plugins officiels{{< /doclink >}}. La nightly est une version instable : testez-la sur une copie de vos données, jamais en production.

## Aider d'autres utilisateurs {#aider}

Vous connaissez bien Galette ? Répondez aux questions posées sur les [GitHub Discussions]({{% param "galette_discussions_url" %}}), sur les [salons de discussion]({{< ref "contact#discussions-instantanées" >}}) (Matrix, Discord, IRC) ou sur la [liste des utilisateurs]({{< ref "contact#listes-de-discussion" >}}). Aider une association voisine à installer ou prendre en main Galette, c'est aussi contribuer.

Vous connaissez un lieu d'entraide autour de Galette qui ne figure pas sur la [page contact]({{< ref "contact" >}}) ? Dites-le nous.

## Faire connaître Galette {#faire-connaitre}

Parlez de Galette sur vos réseaux sociaux, dans votre GULL, lors d'une rencontre entre associations ou d'un salon. Relayez les annonces de nouvelles versions et suivez le projet sur les [réseaux sociaux]({{< ref "contact#réseaux-sociaux" >}}).

## Traduire {#traduire}

Les traductions de Galette, de sa documentation et des plugins officiels se font sur [Weblate](https://hosted.weblate.org/projects/galette/) : créez un compte, choisissez votre langue et traduisez directement dans le navigateur. Vos traductions sont intégrées aux versions suivantes.

La langue source est l'anglais : si vous repérez une erreur dans le texte anglais lui-même, signalez-la plutôt que de la corriger dans une traduction.

{{< img_link path="/site/assets/images/screenshots/weblate.png" alt="Capture d'écran de la plateforme de traduction Weblate" >}}

## Documenter {#documenter}

Certaines fonctionnalités sont peu ou pas décrites dans {{< doclink path="" >}}la documentation{{< /doclink >}}, surtout dans le manuel de l'utilisateur, qui gagne à être écrit par des utilisateurs. Inutile d'écrire de longs textes ou d'être bilingue : le contenu d'origine est en anglais, mais nous pouvons vous aider sur ce point, et chaque contribution est relue.

Pas besoin non plus de maîtriser le format de la documentation : proposez votre texte sur le [gestionnaire de bogues](https://bugs.galette.eu/projects/documentation-galette) ou sur les [GitHub Discussions]({{% param "galette_discussions_url" %}}), nous nous occuperons de la mise en forme. Si vous connaissez Git, une [pull request](https://github.com/galette/galettedoc) est la bienvenue.

## Développer {#developper}

Avant de vous lancer, venez en parler sur les [canaux de discussion]({{< ref "contact" >}}) ou les [GitHub Discussions]({{% param "galette_discussions_url" %}}) : vous saurez si la fonctionnalité a sa place dans Galette et comment l'aborder. Les plugins, souvent assez simples, sont une bonne porte d'entrée, mais les contributions au cœur sont tout aussi bienvenues.

Le code de Galette, des plugins, de la documentation et du site est sur [GitHub](https://github.com/galette) ; les pull requests y sont relues par l'équipe. Toutes les informations utiles pour démarrer sont dans {{< doclink path="source_code.html" branch="develop" >}}la documentation du code source{{< /doclink >}}.

## Faire un don {#donate}

Galette est gratuit, sans version payante ni publicité. Les dons financent le temps consacré à son développement et à sa maintenance, le matériel, et l'hébergement des services du projet (démo, nightly, listes).

* [Faire un don par carte bancaire]({{% param "donate_stripe_url" %}}) via Stripe (des frais de transaction s'appliquent)
* pour un virement, un chèque ou un autre moyen, [contactez-nous]({{< ref "contact" >}})

Merci pour votre soutien !
