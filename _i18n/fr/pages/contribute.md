Vous souhaitez contribuer, mais vous ne savez pas quoi faire ? Peut-être même pensez-vous ne pas pouvoir aider du tout...

Pas de panique, il existe bien des manières de contribuer à un projet comme Galette, il n'est pas nécessaire d'être développeur ;-)

## Utiliser / Tester

Utiliser Galette, c'est déjà soutenir le projet. Assez facile, non ? Allez, merci d'être venus :D

Pour ceux qui seraient restés tout de même, utiliser et tester Galette vont de pair. Donc si vous rencontrez un bogue, ouvrez un ticket avec tous les détails possibles pour qu'un développeur puisse comprendre le problème et le reproduire également, ou utilisez [l'un des canaux de communication]({% tl contact %}) proposés pour exposer votre problème.

Si le cœur vous en dit - surtout maintenant que vous êtes un pro de Galette ! - vous pouvez aussi tester les nouvelles fonctionnalités en développement lorsqu'il y en a, ou essayer régulièrement la [version nightly]({{ site.galette.nightly_url }}).  N'oubliez pas dans ce cas qu'il s'agit d'une version instable ; bien que l'instabilité soit une notion toute relative.

Bien entendu, il en va de même pour les [plugins officiels]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/) :-)

## Aider / Communiquer

Une autre piste potentielle pour contribuer au projet, c'est d'aider à l'installation, à la configuration ou encore à la prise en main de l'outil.

Ce peut-être pour l'association de votre voisin à qui Galette pourrait rendre service, ou qui ne parvient pas à l'installer, par exemple.
Mais ça peut aussi être de réponse à une demande sur les listes ou n'importe quel autre canal de demande d'entre aide. D'ailleurs, si vous connaissez des canaux d'aide Galette existants qui ne sont pas listés dans la page contact, merci de nous les signaler que cela y soit ajouté.

Communiquer autour de Galette est aussi un bon moyen de contribuer, et qui ne demande aucune compétence particulière. Parlez de Galette sur vos réseaux sociaux (les [réseaux sociaux de Galette]({% tl contact%}#réseaux-sociaux) sont listés sur la page contact), dans vos réunions de GUL, ou autres rassemblements.

<a name="donate"></a>
## Faire un don

Une autre manière de contribuer, c'est de faire un don au développeur de Galette, Johan, pour essayer de le motiver un brin ;-)

Vous pouvez ainsi :

* participer à la [cagnotte Galette en cours](https://paypal.me/pools/c/8u4dEPpM0q?locale.x=fr_FR) sur PayPal[^1],
* le contacter pour tout autre moyen (virement, chèque, éventuelle autre plateforme, ...)
* effectuer un [don PayPal](https://www.paypal.me/galettesoft)[^2] (si possible, en dernier recours)

[^1]: Pas de frais appliqués
[^2]: Des frais sont appliqués (environ 1 euro pour un don de 25)

## Traduire

Préambule. Toute contribution au projet doit être faite dans la langue principale (anglais `en_GB`). En cas d'erreur sur la langue principale, il faut aller la corriger dans le contenu d'origine (le code en somme).
N'hésitez pas à utiliser les [canaux de contact]({% tl contact %}) mis à disposition pour trouver de l'aide sur le sujet si vous le souhaitez ;-)

Si donc vous souhaitez aider à traduire Galette, c'est assez simple : rendez-vous sur [la plateforme de traduction (Weblate)](https://hosted.weblate.org/projects/galette/galette/), créez ou liez un compte au besoin, connectez-vous et traduisez !

{% responsive_image path: assets/images/screenshots/weblate.png alt: "Weblate interface" title: "Weblate interface" %}

Pour la documentation, le principe est le même, à la différence que les traduction s'effectuent toujours sur l'ancienne [plateforme de traduction (Zanata)](https://translate.zanata.org/project/view/galettedoc/) (plate forme similaire à Weblate ou Transifex ; mais qui est vieillissante).

{% responsive_image path: assets/images/screenshots/zanata.png alt: "Zanata interface" title: "Zanata interface" %}

Et enfin les plugins... Aucun d'entre eux n'utilise actuellement de système de traduction externe. Le processus nécessite les outils et éditeurs sur le poste de travail, là où un simple navigateur web suffit pour Galette ou la documentation.

### Détails du processus

Si l'on prend l'exemple de Galette, de nouvelles chaînes sources sont ajoutées régulièrement dans le code source. De temps en temps, les chaînes sont extraites du code source (et l'anglais est mis à jour de facto, rien ne devrait différer entre le code source et la traduction anglaise).
Cette opération prend la forme d'un commit sur le dépôt du code source, qui sera automatiquement détecté par le système de traduction une fois publié. La mise à jour de tous les fichiers de langue présents est alors effectuée automatiquement.

Une fois les fichiers de langue à jour, vous pourrez traduire dans la langue de votre choix. Les modifications apportées sont enregistrées sur le système, jusqu'à ce que les développeurs les récupèrent dans le dépôt du logiciel (opération manuelle). Toutes vos traductions seront alors présentes dans Galette !

Hormis pour les plugins, il n'est pas nécessaire de comprendre [l'internationalisation dans Galette](https://translate.zanata.org/project/view/galettedoc/) pour aider à traduire, le paragraphe sur la génération des fichiers de langue vous apportera peut-être quelques précisions davantage techniques.

## Rédiger

Certaines fonctionnalité de Galette sont absentes dans la documentation, ou vraiment détaillées à minima. Là aussi, vous pouvez éventuellement aider en rédigeant de la documentation, ou des articles sur le site. Les principaux manques se situent dans le manuel de l'utilisateur ; parties qui justement devraient pour le mieux être rédigées par des utilisateurs (souvent, le développeur peine à ne pas ajouter moult détails techniques).

La principale contrainte, c'est que les contenus originaux doivent être en anglais. Le but n'est pas d'écrire de grands textes, nul besoin d'être totalement bilingue. Et si vous ne parlez pas du tout anglais, il est toujours possible de vous apporter de l'aide sur ce point.
Les contributions sont dans tous les cas relues et commentées au besoin, permettant d'éventuels ajustements de votre part ou d'un autre participant.

Bien entendu, la documentation se doit de respecter certaines contraintes techniques pour être mise en ligne, mais ce n'est pas un impératif pour de nouveaux ajouts. Si, par exemple, vous ne savez pas faire un lien, il suffira de le préciser d'une manière ou d'une autre dans le contenu, par exemple  `voir l'article xyz (https://xyz.com)`.

Si vous souhaitez compléter la documentation ou y apporter une correction, le fonctionnement est le même que pour Galette : utilisez éventuellement les [canaux de communication]({% tl contact %}) pour exposer votre problématique, dans tous les cas ouvrez un rapport d'anomalie ou une demande d'évolution sur le [gestionnaire de bogues](https://bugs.galette.eu/projects/documentation-galette), pour la suite des opérations  on fera selon les niveaux et les possibilités de chacun.

## Développer / corriger

Avant de vraiment vous lancer, veillez à vous assurer que votre fonctionnalité serait acceptée, ainsi que la manière dont vous souhaitez l'implémenter. Les [différents canaux de communication]({% tl contact %}) servent à ça, n'hésitez surtout pas :)

Nous vous conseillons vivement de lire la [documentation de développement de Galette]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/) afin de vous familiariser un peu avec le code et les règles suivies.

Mettre le nez dans le code, c'est la possibilité de contribution la plus technique. Les plugins seront certainement plus faciles à appréhender que Galette elle-même, la majorité d'entre eux est assez simple ; mais vous pouvez bien sûr proposer des modifications sur le cœur :)
Dans tous les cas de figure, essayez de vous rapprocher du ou des développeur(s) qui sont certainement les personnes les plus à-même de vous aider.

Le code source des différents projets (Galette, plugins, documentation site web) est hébergé dans des dépôts Git, n'importe quel patch applicable par Git fourni de n'importe quelle manière ira très bien. Si vous ne savez pas comment faire, peut-être pouvez vous vous tourner vers le miroir GitHub correspondant, certains d'entre eux sont déjà utilisés pour les travaux en incubation pour ne pas encombrer le dépôt principal. Dans le cas de GitHub, on passera par une PR (Pull Request) qui sera revue par l'équipe de développement.

Toutes les [informations fort utiles au code source de Galette ou des plugins sont disponibles dans la documentation de développement]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html).
