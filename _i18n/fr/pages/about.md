Galette est une application web de gestion d'adhérents pour les associations. Galette est écrit en PHP et utilise une base de données [MariaDB](https://mariadb.org) ou [PostgreSQL](https://postgresql.org). C'est un **logiciel libre**, sous [licence GPL](https://www.gnu.org/licenses/quick-guide-gplv3.fr.html).

Depuis 2007 (voir ci-dessous [l'histoire de Galette](#histoire-de-galette)), Johan est le développeur, mainteneur et homme à tout faire. Des contributions externes ont toujours été régulièrement intégrées.

## Le projet

Depuis le début, il a été défini que l'axe principal du projet serait la gestion des adhérents et adhésions. La question par exemple d'inclure des notions de comptabilité a été évoquée, mais refusée, car trop éloignée à notre sens de cet axe (sans compter la charge supplémentaire que ça impliquerait en termes de développements et de maintenance).

Outre ce type de « limites », les fonctionnalités intégrées au cœur du logiciel se veulent le plus générique possible, ce afin de convenir au plus grand nombre. Certaines fonctionnalités plus spécifiques n'y ont pas leur place, mais peuvent en revanche être ajoutées par le biais du système des plugins : l'on peut ainsi depuis Galette [gérer un club automobile]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/auto.html) ou  utiliser un [système de prêts d'objets]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/objectslend.html).

Le système de [gestion des tickets]({{ site.galette.tracker_url }}) ainsi que le [système de vote]({{ site.galette.vote_url }}) vous permettent d'influencer les futures fonctionnalités, mais vous pouvez bien entendu les [ajouter vous-mêmes]({% tl contribute %}) :-)

Un certain nombre de fonctionnalités demandées (lien avec des services tiers par exemple) auraient tout à fait leur place dans Galette, mais ce sont des tâches complexes pour lesquelles il n'a pour le moment pas été possible de dégager du temps.

De nouvelles fonctionnalités sont tout de même ajoutées régulièrement, faisant diminuer un peu la liste des choses à faire (qui ne cesse de grandir par ailleurs ;)).

Le projet n'a pas de cycle de sortie défini : « ça sort quand c'est prêt ». Toutefois, la sortie de versions correctives est faite assez régulièrement, soit lorsqu'un problème important est détecté, soit lorsque plusieurs problèmes ont déjà été réglés, ou encore si c'était demandé (ça n'est encore jamais arrivé).

Enfin, notez qu'une seule version majeure n'est supportée à la fois. Ainsi, depuis la sorte de Galette 0.9 ; la version 0.8 n'est plus supportée. La seule exception à cette règle, ce serait pour corriger une faille de sécurité, si toutefois la nouvelle majeure est assez récente. La question ne s'est posée qu'une seule foir pour le moment.

## Ils utilisent Galette

La <a href="https://telemetry.galette.eu/reference" hreflang="en">liste des utilisateurs de Galette</a> peut être consultée sur notre application de télémétrie :)
<a href="http://telemetry.galette.eu/reference?showmodal" hreflang="en">Enregistrez-vous si vous utilisez Galette</a> !

Notez que vous pouvez également [vous enregistrer depuis Galette]({{ site.galette.doc_url }}/{{ site.lang }}/master/usermanual/generalites.html#telemetry) (à partir de la version 0.9) ; ce qui vous permettra par la suite de modifier vos données.

## Histoire de Galette

L'[ALDIL](https://www.aldil.org/), GULL de Lyon, se cherchait un système de gestion des adhérents (vers 2000 ~ 2001). Après avoir testé PhpLugMembers et quelques autres outils, rien ne convenait.
Le président de l'ALDIL de l'époque (Loïs, aka GruiicK) a alors décidé de lancer un appel d'offre sur les listes de l'ALDIL.

Le premier projet, nommé GAELLE, est rapidement mort. Code un peu compliqué et developpeurs pas trés motivés/présents.

En 2003, Frédéric (aka Deelight) repart de zéro et commence à coder une appli jolie, sans prétention, et, comme il le disait lui-même à l'époque : « fait ce qu'on lui demande ».

La première version "stable" a du être la version 0.37b. Jusqu'en 2005, le projet évolue tranquillement, par l'ajout de nouvelles fonctionnalités, et par l'arrivé de nouveaux développeurs / traducteurs / relecteurs / béta-testeurs (merci à eux).

Début 2007, Johan (aka trashy) rejoint le projet. En mai, Loïs lui cède les "clefs du camion" et Johan prend la responsabilité du projet Galette.

Le projet est hébergé sur `Gna!` depuis 2004. Début 2005, un projet Galette a également été créé chez [TuxFamily](https://tuxfamily.org).
Gna est en charge de l'hébergement du dépôt SVN, des listes de diffusion et des tracker ; tandis que TuxFamily se charge de l'hébergement du site web et des téléchargements.

Courant 2012, le code source du projet passe à Git ; l'hébergement des dépôts de fait chez Tuxfamily également. Le tracker Gna! est également abandonné.

Début 2017, les listes de diffusion passent également chez Tuxfamily, Gna ayant annoncé la fin de leurs bons et loyaux services.

### Mail Originel

Ceci est le **mail originel** annonçant la création de Galette. Depuis, la liste Code de l'[ALDIL](https://www.aldil.org) a disparu, ses archives aussi.
De même, le premier site wiki du projet a disparu aussi...

<pre>
Message-ID: &lt;033501c3afbf$e6f954a0$0200a8c0@deetanic&gt;
From: Frédéric Jacquot &lt;deelight _AT_ poulet.org&gt;
To: &lt;code _AT_ listes.aldil.org&gt;
Subject: [Code] Une petite Galette pour la route ?
Date: Fri, 21 Nov 2003 00:41:58 +0100

Hello,

Comme je n'ai toujours pas posté ici concernant Galette, je le fais.
Comme il est assez tard, je serai bref, quitte à être plus bavard par la
suite :)

Tout est dispo sur le wiki de Galette (sources, un peu de doc, demo...) :
http://www.zopeuse.org/projets/galette/Wiki_galette/FrontPage

C'est certainement assez brut de décoffrage mais ça fait ce qu'on lui
demande. Si certains se sentent de fouiller un peu de le code pour voir s'il
peuvent y apporter leur touche personelle, n'hésitez pas à me le dire et je
mettrai les mains dans le camboui pour monter un CVS pour l'occasion si
nécessaire.

Comme le montre la Todolist du wiki, il reste pas mal de choses, notamment
essayer de tuner tout ça pour que ca tourne sur du PostgresSQL (j'utilise la
librairie ADODB donc à priori, on doit pouvoir y arriver sans trop de mal),
puisque c'est ce qui sera utilisé en définitif.

Actuellement, ça s'installe et sa tourne sans problème apparent sur du
MySQL.
Je serais vraiment content d'avoir des retours constructifs pour pouvoir
améliorer l'appli et plus globalement ma façon de coder.

Wiki, mail, forum... il y a le choix ;)

Deelight
----
ALDIL - Code (Code _AT_ listes.aldil.org)
https://listes.aldil.org/mailman/listinfo/code
</pre>

### D'où vient le nom Galette

Les membres de l'[ALDIL](https://www.aldil.org/) ont longuement cherché un nom pour ce logiciel. Voici un rapide résumé.

Sachez qu'au final, Deelight (Développeur : Celui qui a raison) a choisi Galette, GruiicK (Président : Celui qui dit banco) a dit banco.

<pre>  TATMonMembre : Trafic Admin Threaders &amp; Monitor of Members,
  GAMELL : Gestion et Administration des Membres En-Ligne de LUG,
  MAEL : Management et Administration En-ligne d'un Lug,
  SUGEM : Systeme Universel de Gestion En_ligne des Membres,
  SAGEM : Systeme d'Administration et de Gestion En ligne des Membres,
  SAGIMP : Systeme d'Administration Gestion Interactive des Membres en Php,
  ALP : Administration d'un Lug en Php,
  SCALP : Systeme Complet d' Administration d'un Lug en Php,
  LAT : Lug Administration ToolKit,
  SALUG : Systeme d'Administration LUG (&lt;= acronyme déjà pris, LUG existant),
  AGMA : Aide à la Gestion de Membres d'Association,
  GIM : Gestion Interactive de Membres,
  SAL : Systeme d'Administration Libre,
  GAIA : Gestion Administration Interactive d'Association,
  SASGLUG : Systeme d'Administration Simplifié pour la Gestion d'un LUG,
  LUGDUNUM : LUG Data User NUmeric Manager (nom latin de Lyon, aussi),
  LATeK : Lug Administration Tool e-Kit  (ou, e-ToolKit ?),
  LArT  : Lug Administration Tool  (spécial BOFH),
  SIGMA : Special Interests Groups Management Application,
  KATMANDOU : Kit d'Administration et Trésorerie des Membres d'Association Nonlucrative,
  GELA : Gestion En Ligne d'Association,
  GASEL : Gestion Administration Simplifiée En Ligne &lt;= acronyme déjà pris (linux-nante),
  GASOL : Gestion Administration Simplifiée On-Line,
  GIM : Gestion Interactive de Membres,
  SAL : Systeme d'Administration Libre, qui assemblés donnent :
  SALGIM : Systeme d'Administration Libre de Gestion Interactive de Membres,
  GAIMA : Gestion Administration Interactive de Membres d'Association,
  GALETTE : Gestionnaire d'Adhérents en Ligne Extrèmement Tarabiscoté mais Tellement Efficace,
  GAELLE : Gestion d'Association En Ligne pour Lug Et autres,
  SELMA : Suivi En Ligne des Membres d'Associations,
  SALAMI : Systeme d'Administration en Ligne d'Association et ses Membres Interactifs,
  GALIA : Gestion et Administration L(inuxienne et) Interactive d'Association.</pre>

## Fortunes

(section des fortunes mail/irc/etc, par ordre anti-chronologeek)

<pre>
* trashy_ en panne d'inspi pour une annonce des 10 ans :'''''(
&lt;GruiicK&gt; pique un slogan à monoprix
&lt;GruiicK&gt; ou un martine cover generator
&lt;GruiicK&gt; elle a +/- tout le temps 10 ans, martine, non ?
&lt;bohwaz_&gt; lol
&lt;GruiicK&gt; moi, j'aime bien l'équipe marketing monoprix
&lt;GruiicK&gt; galette des rois : patisserie à suspense
&lt;GruiicK&gt; beurre doux : gouté et approuvé par le petit chaperon rouge
&lt;GruiicK&gt; &quot;tout est dans le coup de roquette&quot; (paquet de salade fragmentée, roquette)
&lt;GruiicK&gt; batonnets de crabe : une découverte majeure : le poisson-frite !
</pre>

<pre>
&lt;GruiicK&gt; bon, re-init passwd dc = ok
&lt;GruiicK&gt; et entre temps, j'ai oublié la modif que je voulais faire...
&lt;GruiicK&gt; deux neurones
&lt;trashy_&gt; mdr
</pre>

<pre>
&lt;GruiicK&gt; po grave, je brode avec ce qui existe sur le site de galette :)
* trashy savait pas que GruiicK faisait de la broderie...
&lt;trashy&gt; tu fais ça le dimanche, pour passer le temps ?
&lt;trashy&gt; et tu saurais en parler en public ? au cours d'un dîner par exemple ?
</pre>

<pre>
&lt;trashy&gt; ça va donner plus de visibilité aux fortunes, et ça, c'est hyper cool : on va pouvoir dire plein d'âneries :o]
* trashy va prendre son calmant.
</pre>

<pre>
&lt;hertay&gt; Trashy, dans http://galette.eu c'est toujours la 0755 qui est en téléchargement (lien) ;-)
&lt;trashy_&gt; c'est la faute à GruiicK ! :p
&lt;GruiicK&gt; mééé heu !!
&lt;trashy_&gt; :o)
&lt;GruiicK&gt; de toute façon, les codes numériques chown, c'est source d'erreur, il faut utiliser la convention ugo.
&lt;GruiicK&gt; &quot;C'est qui ugo ?&quot;
</pre>

<pre>
&lt;trashy&gt; un mec a édité une page du wiki de l'april en novembre pour spécifier que Galette n'était plus développé...
&lt;trashy&gt; je vais lui faire bouffer le listing des diffs que j'ai commité en novembre tiens ; ça lui apprendra. 
</pre>

<pre>
&lt;trashy_&gt; j'ai trouvé un slogan pour Galette : « Il y a un champ dynamique pour cela. » © :D
&lt;GruiicK&gt; bouahahahahaha
&lt;GruiicK&gt; adopté !
&lt;trashy_&gt; ^_^
</pre>

<pre>
--&gt; LaoTseu (~alex@home.laotseu.org) has joined #galette
&lt;LaoTseu&gt; huhu ca existe :)
&lt;GruiicK&gt; LaoTseu: tu veux coder sur galette aussi ?
&lt;LaoTseu&gt; GruiicK: ouais on m'a dit que je pouvais devenir riche et celebre :)
&lt;stephs&gt; :))
&lt;GruiicK&gt; célèbre, ouais, riche, c'est pas prouvé
&lt;LaoTseu&gt; mais je pense qu'on s'est encore foutu de ma gueule
&lt;stephs&gt; GruiicK: sisi, avec des vierges à gros seins et tout et tout
&lt;LaoTseu&gt; :D
&lt;GruiicK&gt; hop, fortune
&lt;stephs&gt; :)
</pre>

<pre>
&lt;-- Deelight has quit (Ping timeout: 480 seconds)
&lt;-- stephs has quit (Ping timeout: 480 seconds)
&lt;GruiicK&gt; hé ben voilà, comme d'hab', j'suis tout seul face à la meute...
</pre>

<pre>
&lt;Deelight&gt; je me penche sur la modif sur la table des preferences
&lt;stephS&gt; penche toi pas trop non plus
&lt;stephS&gt; &lt;/je fais des blagues lourdes et j'assume&gt;
&lt;GruiicK&gt; je log les fortunes et j'assume.
&lt;Deelight&gt; attention, j'assomme.
</pre>

<pre>
&lt;GruiicK&gt; Deelight: faudrait un lien direct vers la demo de galette sur la
          page d'accueil de gna
&lt;-- Deelight has quit (Read error: No route to host)
&lt;GruiicK&gt; forcément, il se planque, le lâche :)
&lt;stephS&gt; Deelight: allez reviens il disait ca pour rire
</pre>

<pre>
&lt;GruiicK&gt; ben ça marche qd mm
&lt;stephS&gt; vivi, je dis juste au cas où zavions pas remarquer
&lt;GruiicK&gt; zavions vu
&lt;stephS&gt; zavions super fort alors :)
&lt;GruiicK&gt; et zavions supersonique
</pre>

<pre>
&lt;GruiicK&gt; j'essaie
&lt;Deelight&gt; :
&lt;Deelight&gt; )
&lt;Deelight&gt; (smiley ikea)
&lt;GruiicK&gt; ah, ikéa, je gère, ça donne ça : &quot;:)&quot;
&lt;GruiicK&gt; mais y'a pas les outils livrés, t'aura droit à une réclamation
&lt;Deelight&gt; :)
&lt;Deelight&gt; attends, la celebre clé alène
&lt;Deelight&gt;  ____|
&lt;Deelight&gt; |
&lt;Deelight&gt; voilà
&lt;GruiicK&gt; merci.
&lt;Deelight&gt; | | | | |
&lt;Deelight&gt; (les ptits machins en bois a mettre dans les ptits trous)
&lt;stephS&gt; tous des drogués.
&lt;GruiicK&gt; alleï, inauguration du fichier de fortune
&lt;Deelight&gt; :)
&lt;stephS&gt; ouiii :)
</pre>

## Outils utilisés

La gestion d'un projet comme Galette requiert qu'un certain nombre de solutions techniques soient mises en oeuvre : [moyens de communication]({% tl contact %}), [hébergement du code source](https://git.tuxfamily.org/galette/), [gestion des tickets]({{ site.galette.tracker_url }}), ...). Voici ce qui est utilisé :

* [code source](https://git.tuxfamily.org/galette/) : [Git](https://git-scm.com/), hébergé chez [TuxFamily](https://tuxfamily.org),
* site web : généré par [Jekyll](https://jekyllrb.com)[^1], hébergé chez TuxFamily,
* [gestionnaire de tickets]({{ site.galette.tracker_url }}) : [Redmine](https://redmine.org)[^2], hébergé sur un serveur dédié,
* [démo](https://demo.galette.eu) : [Galette](https://galette.eu), hébergée sur un serveur dédié,
* [listes de diffusion]({% tl contact %}#listes-de-discussion) : [VHFFS](https://vhffs.org)[^3], fournies par TuxFamily,
* [système de vote]({{ site.galette.vote_url }}) : [Fider](https://fider.io), hébergé sur Fider,
* [documentation]({{ site.galette.doc_url }}/{{ site.lang }}/master) : générée par [Sphinx](https://www.sphinx-doc.org)[^4], hébergée chez [ReadTheDocs](https://rtfd.org),
* [traductions]({{ site.galette.trad_url }}) : [Weblate](https://weblate.org)[^5], hébergé chez Weblate.
* [traduction documentation](https://translate.zanata.org/project/view/galettedoc/) : [Zanata](http://zanata.org)[^6], hébergé chez Zanata.
* Johan, hébergé chez lui :p

Bien que ce ne soit pas un outil libre, [Galette possède des miroirs officiels sur GitHub](https://github.com/galette), pour plusieurs raisons :

* l'espace est limité chez TuxFamily. En utilisant GitHub pour les branches de développement, on évite ainsi de grossir inutilement le dépôt Git principal,
* beaucoup de gens ont un compte GitHub, très peu un compte TuxFamily,
* proposer une modification est aisé pour les utilisateurs,
* le système de revue est pratique,
* pas besoin de gérer un service supplémentaire (la liste est déjà longue),
* services d'intégration continue (les tests sont lancés à chaque commit),
* l'interface web aide à chercher/naviguer dans le code, c'est moins évident avec le CGIT du dépôt officiel,
* il n'est pas possible de créer des hooks git chez TuxFamily, or c'est utilisé pour mettre à jour les traductions et la documentation ainsi que pour lancer les tests :/

[^1]: depuis 2020. Le site était propulsé par [Dotclear](https://dotclear.org) entre 2012 et 2020, et par [dokuwiki](https://dokuwiki.org) avant 2012
[^2]: depuis 2012. Avant cela, le système proposé par Gna! était utilisé
[^3]: depuis 2017. Avant cela, les listes étaient gérées par [Mailman](https://list.org/) chez Gna! jusqu'à la fermeture de lerus services
[^4]: depuis 2012. Tout était sur le site web avant cette date
[^5]: depuis 2019. Les traductions étaient gérées entièrement en local auparavant
[^6]: depuis 2019. La documentation n'était disponible qu'en français avant cela
