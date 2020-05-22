Il existe bien des façons de contribuer à un projet comme Galette. En voici une liste non exhaustive :

* support aux utilisateurs sur les [listes de diffusion]({% tl contact %}#listes-de-discussion) ou (plus rarement) sur le [canal IRC]({% tl contact %}#irc),
* [traduction](https://hosted.weblate.org/projects/galette/galette/) (de Galette, mais aussi de la documentation),
* [développement du code en lui même]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/index.html),
* rédaction des diverses documentations ([guide d'installation]({{ site.galette.doc_url }}/{{ site.lang }}/master/installation/index.html), [guide de l'utilisateur]({{ site.galette.doc_url }}/{{ site.lang }}/master/usermanual/index.html), [guide du développeur]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/index.html), [questions fréquentes]({{ site.galette.doc_url }}/{{ site.lang }}/develop/faq/index.html), ...),
* [développement, documentation et tests de plugins]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/index.html),
* test des versions de développement,
* [faire un don au développeur de Galette](https://www.paypal.me/galettesoft) (contactez-le si vous préférez utiliser un chèque ou un virement),
* ...

Si participer à Galette vous tente, n'hésitez plus !

Il y a tout de même quelques petites choses à savoir avant de commencer... :)

## Le code de Galette

Toutes les [informations fort utiles au code source de Galette ou des plugins sont disponibles dans la documentation de développement]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html).


### Tester

Tester le code de Galette se résume généralement à l'installer et à l'utiliser :-) Aucune connaissance technique particulière n'est requise.

Les différents moyens de contact sont à votre disposition pour obtenir de l'aide ou des conseils, les différents trackers vous permettront de rapporter les bogues rencontrés, de demander d'éventuelles améliorations ou fonctionnalités, et éventuellement de soumettre des patchs.

## La documentation de Galette

Le code source de la documentation de Galette est hébergé sur un dépôt GIT, <a href="{{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html">référez-vous à la documentation pour plus de détails</a>.

La documentation est rédigée en utilisant le format <a href="http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html" hreflang="en">reStructuredText</a> et est construite avec <a href="http://sphinx.pocoo.org/" hreflang="en">Sphinx</a>.

Ces informations peuvent vous paraître un poil techniques, mais somme toute, la documentation est rédigée via de simples fichiers textes, avec un syntaxe particulière (fort bien documentée) s'apparentant quelque peu à une syntaxe wiki ; tout en offrant de nombreuses fonctionnalités supplémentaires ; il ne faut donc pas de connaissances techniques particulières ici non plus.

## Le site de Galette

Le site de Galette est propulsé par DotClear. Le <a href="https://bitbucket.org/trashy/galette_dc_theme">thème DotClear pour Galette est disponible via un dépôt GIT</a>. Si vous corrigez une erreur ; je serai ravi de l'intégrer ;-)

## Les traductions

Les traductions dans Galette sont basées sur gettext via des fichiers po. Il existe différents outils d'édition de fichiers PO ; qui permettent de trouver facilement les chaînes nouvelles, modifiées ou absentes. Une partie de la [documentation de la Galette traite spécifiquement l'internationalisation]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/i18n.html), si vous souhaitez en savoir d'avantage.

Vous pouvez [aider à la traduction](https://hosted.weblate.org/projects/galette/galette/) elle même depuis la plateforme de traduction !
