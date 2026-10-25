---
title: "Plugins"
seo_title: "Plugins Galette : paiement en ligne, événements, prêt de matériel, carte des adhérents"
slug: "plugins"
description: "Étendez Galette, logiciel libre de gestion d'association, avec ses plugins gratuits : paiement en ligne HelloAsso, événements, activités, prêt de matériel, carte des adhérents, connexion unique."
---
Galette se concentre sur l'essentiel : la [gestion des adhérents]({{< relref "members.md" >}}), des [cotisations]({{< relref "fees.md" >}}) et la [communication]({{< relref "communication.md" >}}). Ce qui ne sert qu'à une partie des associations passe par des **plugins** : vous n'installez que ce dont vous avez besoin, et le cœur reste simple.

Les plugins sont libres et gratuits, comme Galette. Une fois copiés dans le dossier `plugins` de votre installation, ils s'activent et créent leurs tables depuis la page des plugins de Galette, sans ligne de commande.

## Paiement en ligne

* [**HelloAsso**](https://galette-plugins.github.io/plugin-helloasso/) : vos adhérents paient leur cotisation ou font un don par HelloAsso, la plateforme de paiement des associations françaises, et la contribution est enregistrée dans Galette dès que le paiement est validé.
* [**Stripe**](https://galette-plugins.github.io/plugin-stripe/) : le même principe avec Stripe, pour les cotisations et les dons.

## Activités et événements

* [**Events**](https://galette-plugins.github.io/plugin-events/) : organisez des événements et gérez les réservations de vos adhérents.
* [**Activities**](https://galette-plugins.github.io/plugin-activities/) : gérez les activités de l'association et les inscriptions des adhérents à chacune d'elles.

## Matériel et véhicules

* [**ObjectsLend**](https://galette-plugins.github.io/plugin-objectslend/) : prêt et location de matériel aux adhérents, avec le suivi de qui a emprunté quoi.
* [**Auto**](https://galette-plugins.github.io/plugin-auto/) : pour les clubs automobiles, les véhicules de chaque adhérent et leur historique.

## Carte des adhérents

[**Maps**](https://galette-plugins.github.io/plugin-maps/) géolocalise les adhérents et affiche sur une carte ceux qui ont accepté d'être visibles. La carte s'appuie sur OpenStreetMap : pas de clé d'API ni d'inscription, et tout peut être auto-hébergé.

## Connexion unique

[**OAuth2**](https://galette-plugins.github.io/plugin-oauth2/) fait de Galette un serveur d'authentification : vos adhérents se connectent avec leur compte Galette sur d'autres outils de l'association, comme un Nextcloud ou un forum Flarum. Un seul mot de passe, et l'accès suit l'adhésion.

## Mentions légales

[**LegalNotices**](https://galette-plugins.github.io/plugin-legalnotices/) ajoute des pages de mentions légales, et peut gérer le consentement aux cookies si vous intégrez des services externes.

## Qui maintient les plugins ?

Tous les plugins sont rassemblés sur [l'organisation galette-plugins](https://github.com/galette-plugins/). Une partie est développée par l'équipe de Galette, en même temps que le cœur ; les autres sont maintenus par leurs auteurs, membres de la communauté. Chaque site de plugin indique sa compatibilité et son mode d'installation.

Un besoin qui n'est pas couvert ? Les plugins peuvent ajouter des pages, des menus, des préférences et des pages publiques : écrivez le vôtre et {{< doclink path="plugins/plugins-tiers.html" >}}proposez-le à l'organisation{{< /doclink >}}, ou [contactez-nous]({{< relref "contact.md" >}}) pour en parler.

Pour aller plus loin :

* {{< doclink path="plugins/index.html" >}}la documentation des plugins{{< /doclink >}},
* [Pourquoi Galette ?]({{< relref "why.md" >}}),
* [la démo en ligne](https://demo.galette.eu/), où plusieurs plugins sont activés.
