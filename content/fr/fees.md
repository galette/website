---
title: "Gestion des cotisations"
seo_title: "Logiciel de gestion des cotisations d'association, libre et gratuit"
slug: "gestion-des-cotisations"
description: "Gérez les cotisations de votre association avec Galette, logiciel libre et gratuit : échéances calculées, relances automatiques, dons, paiements fractionnés, reçus et factures en PDF."
---
Qui est à jour de cotisation ? Qui faut-il relancer ? Combien les dons ont-ils rapporté cette année ? Galette répond à ces questions sans tableur ni calcul de tête : chaque cotisation enregistrée met à jour la **date d'échéance** de l'adhérent, et tout le reste en découle.

## Des cotisations à votre façon

Chaque association a ses règles, Galette s'y adapte :

* des **types de cotisation** que vous définissez : cotisation annuelle, tarif réduit, cotisation mensuelle ou trimestrielle, avec un montant proposé par défaut,
* des **dons** et autres contributions qui ne prolongent pas l'adhésion,
* une **période d'adhésion** commune à tous (par exemple du 1<sup>er</sup> septembre au 31 août) ou une durée qui court à partir du paiement,
* des **mois offerts** en fin de période : avec deux mois offerts, une cotisation payée en novembre vaut pour toute l'année suivante,
* des adhérents **dispensés de cotisation**, membres d'honneur ou bénévoles.

## Toujours savoir qui est à jour

L'échéance de chaque adhérent est calculée automatiquement, et la liste des adhérents affiche d'un coup d'œil qui est à jour, qui arrive à échéance et qui est en retard. Chaque adhérent voit aussi, dans son espace, le nombre de jours restants ou son retard.

La liste des cotisations se filtre par date, par type ou par moyen de paiement, avec le total des montants trouvés. La recherche avancée sait retrouver, par exemple, tous les adhérents dont la cotisation expire dans le mois.

{{< img_link path="/site/assets/images/screenshots/contributions_list.png" alt="Liste des cotisations, avec ses filtres" >}}

## Des relances qui partent toutes seules

Galette prépare les **relances par email** : un mois puis sept jours avant l'échéance, puis un et deux mois après. Chaque relance est écrite dans la langue de son destinataire, et Galette propose d'imprimer des étiquettes pour les adhérents sans adresse email.

Vous pouvez envoyer les relances depuis le tableau de bord, ou les **automatiser** avec une tâche planifiée sur votre serveur ; les limites d'envoi de votre messagerie sont respectées.

## Paiements, transactions et reçus

* Une **transaction** regroupe un paiement unique réparti sur plusieurs cotisations : le chèque d'une famille qui paie trois adhésions et un don, par exemple.
* Les **paiements échelonnés** répartissent une cotisation en plusieurs versements.
* Chaque cotisation peut produire son **reçu** ou sa **facture** en PDF, sur un modèle que vous personnalisez ; les adhérents les retrouvent dans leur espace.
* Le **paiement en ligne** s'ajoute avec les [plugins]({{< relref "plugins.md" >}}) [HelloAsso](https://galette-plugins.github.io/plugin-helloasso/) ou [Stripe](https://galette-plugins.github.io/plugin-stripe/) : la cotisation est enregistrée dès que le paiement est validé.

## Et le reste ?

Les cotisations sont indissociables de la [gestion des adhérents]({{< relref "members.md" >}}). Galette n'est pas un logiciel de comptabilité, mais les exports CSV permettent de reprendre ces données dans l'outil de votre trésorier. [Pourquoi Galette ?]({{< relref "why.md" >}}) explique ces choix.

Pour aller plus loin :

* {{< doclink path="usermanual/contributions.html" >}}le manuel de la gestion des cotisations{{< /doclink >}},
* {{< doclink path="usermanual/reference_lists.html" >}}la configuration des types de cotisation{{< /doclink >}},
* [la démo en ligne](https://demo.galette.eu/) pour essayer sans rien installer.
