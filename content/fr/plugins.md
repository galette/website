---
title: "Plugins"
seo_title: "Plugins Galette : paiement en ligne, événements, prêt de matériel, carte des adhérents"
slug: "plugins"
description: "Étendez Galette, logiciel libre de gestion d'association, avec ses plugins gratuits : paiement en ligne HelloAsso, événements, activités, prêt de matériel, carte des adhérents, connexion unique."
---
<p class="lead">Galette se concentre sur l'essentiel : la <a href="{{< relref "members.md" >}}">gestion des adhérents</a>, des <a href="{{< relref "fees.md" >}}">cotisations</a> et la <a href="{{< relref "communication.md" >}}">communication</a>. Le reste passe par des <strong>plugins</strong>, libres et gratuits : vous n'installez que ce dont vous avez besoin, et le cœur reste simple.</p>

{{< img_link path="/site/assets/images/screenshots/1.3.2/plugins-updates-fr.png" alt="La page des plugins dans Galette" >}}

## Paiement en ligne

{{< cards class="two-cols" >}}
{{< card icon="card" title="HelloAsso" url="https://galette-plugins.github.io/plugin-helloasso/" button="Site du plugin" >}}
Cotisations et dons payés par HelloAsso, la plateforme des associations françaises ; la contribution est enregistrée dès le paiement validé.
{{< /card >}}
{{< card icon="card" title="Stripe" url="https://galette-plugins.github.io/plugin-stripe/" button="Site du plugin" >}}
Le même principe avec Stripe, pour les cotisations et les dons.
{{< /card >}}
{{< /cards >}}

## Activités et événements

{{< cards class="two-cols" >}}
{{< card icon="calendar" title="Events" url="https://galette-plugins.github.io/plugin-events/" button="Site du plugin" >}}
Organisez des événements et gérez les réservations de vos adhérents.
{{< /card >}}
{{< card icon="checklist" title="Activities" url="https://galette-plugins.github.io/plugin-activities/" button="Site du plugin" >}}
Gérez les activités de l'association et les inscriptions des adhérents à chacune d'elles.
{{< /card >}}
{{< /cards >}}

## Matériel et véhicules

{{< cards class="two-cols" >}}
{{< card icon="package" title="ObjectsLend" url="https://galette-plugins.github.io/plugin-objectslend/" button="Site du plugin" >}}
Prêt et location de matériel aux adhérents, avec le suivi de qui a emprunté quoi.
{{< /card >}}
{{< card icon="car" title="Auto" url="https://galette-plugins.github.io/plugin-auto/" button="Site du plugin" >}}
Pour les clubs automobiles : les véhicules de chaque adhérent et leur historique.
{{< /card >}}
{{< /cards >}}

## Carte des adhérents, connexion unique et mentions légales

{{< cards >}}
{{< card icon="pin" title="Maps" url="https://galette-plugins.github.io/plugin-maps/" button="Site du plugin" >}}
Une carte des adhérents qui ont accepté d'y figurer, sur OpenStreetMap : sans clé d'API, auto-hébergeable.
{{< /card >}}
{{< card icon="key" title="OAuth2" url="https://galette-plugins.github.io/plugin-oauth2/" button="Site du plugin" >}}
Vos adhérents se connectent avec leur compte Galette à vos autres outils (Nextcloud, Flarum…) : l'accès suit l'adhésion.
{{< /card >}}
{{< card icon="file" title="LegalNotices" url="https://galette-plugins.github.io/plugin-legalnotices/" button="Site du plugin" >}}
Des pages de mentions légales, et la gestion du consentement aux cookies si vous intégrez des services externes.
{{< /card >}}
{{< /cards >}}

## Installer un plugin

{{< steps >}}
1. **Téléchargez** le plugin depuis son site, qui indique aussi les versions de Galette compatibles.
2. **Décompressez-le** dans le dossier `plugins` de votre installation de Galette.
3. **Activez-le** depuis la page des plugins de Galette, qui crée aussi ses tables : pas besoin de ligne de commande.
{{< /steps >}}

Tous les détails sont dans {{< doclink path="plugins/index.html" >}}la documentation des plugins{{< /doclink >}}. Pour voir plusieurs plugins en action, essayez [la démo en ligne](https://demo.galette.eu/).

## Qui maintient les plugins ?

Tous les plugins sont rassemblés sur [l'organisation galette-plugins](https://github.com/galette-plugins/). Une partie est développée par l'équipe de Galette, en même temps que le cœur ; les autres sont maintenus par leurs auteurs, membres de la communauté.

Un besoin qui n'est pas couvert ? Les plugins peuvent ajouter des pages, des menus, des préférences et des pages publiques : écrivez le vôtre et {{< doclink path="plugins/plugins-tiers.html" >}}proposez-le à l'organisation{{< /doclink >}}, ou [contactez-nous]({{< relref "contact.md" >}}) pour en parler.
