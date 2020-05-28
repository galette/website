Galette is a web application to manage adherents for associations. Galette is written in PHP and rely on [MariaDB](https://mariadb.org) or [PostgreSQL](https://postgresql.org). This is a **free software** (as in free speech), under the terms of the [GPL licence](https://www.gnu.org/licenses/quick-guide-gplv3.fr.html).

Since 2007 (see below [the history of Galette](#galettes-history)), Johan is the developer, maintainer and handyman. External contributions has always been integrated regularly.

The name Galette is a French acronym for “Gestionnaire d’Adhérents en Ligne Extrêmement Tarabiscoté mais Tellement Efficace”, freely translated to “Extremely Sophisticated but so Efficient On-Line Membership Manager”. The french word “galette” also means (popular) “Money”. Unfortunately, the translation removes all the fun!

## The project

Since the beginning, it has been defined that the main project axis is to manage members and membership. The question of integrating as example accounting features has been asked, but declined, because too far in our minds from this axis (without taking into account the cost it can have on development and maintenance).

Apart this kind of "limit", features that reach Galette core try to be as generic as possible, to suit the most of the needs. Some more specific features does not have place in core, but can be added from plugins: therefore it is possible form Galette to [manage an automobile club]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/auto.html) or use a [loan objects system]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/objectslend.html).

[Bug tracking system]({{ site.galette.tracker_url }}) as well as [voting system]({{ site.galette.vote_url }}) let you influence future features, but you can of course [add them yourself]({% tl contribute %}) :-)

Some of requested features (link to third party services as example) would have their place into Galette, but are complex tasks for which it has not been yet possible to find time.

New features are still regularly added, reducing the todo list (which always gets bigger ;)).

The project does not have any release cycle: "It's released when it's cooked". Anyway, bugfixes releases are quite regular, when a major issue has been found, or when several ones has been addressed, or if we were asked for (it has never happen yet).

Finally, note that only one major release is supported. Then, since Galette 0.9 has been released, 0.8 is no longer supported. The only exception to this rule would be a fix for a security issue, if new major is quite recent. This happened only once for now.

## They use Galette

[Galette's users list](https://telemetry.galette.eu/reference) is available from our telemetry application :)
[Register yourself if you use Galette](https://telemetry.galette.eu/reference?showmodal)

Note that you can also [register from Galette]({{ site.galette.doc_url }}/{{ site.lang }}/master/usermanual/generalites.html#telemetry) (since 0.9); you will be able to edit your data using this.

## Galette's history

[ALDIL](https://www.aldil.org), LUG from Lyon (France), was looking for a membership management application (around 2000~2001). After tests of PhpLugMembers and some other tools, nothing was doing the trick.
ALDIL's former president (Loïs, aka GruiicK) decided to invite tenders on ALDIL lists.

The first project, whose name was GAELLE, dies quickly. Code was a bit complex, and developpers were not very involved/presents.

In 2003, Frédéric (aka Deelight) started from scratch a nice application, unpretentious, and, as he said himself: « do what it gotta do ».

The first "stable" version has probably been version 0.37b. Since, project continues quietely to change, by adding new functionnalities, and by receiving new developpers / translators / reviewers / testers (many thanks to them).

In early 2007, Johan (aka trashy) joined the project. In April, Loïs gives him the "keys of the truck" and Johan took charge of the project Galette.

Project is hosted on `Gna!` since 2004. Early 2005, a project Galette is also opened at [TuxFamily](https://tuxfamily.org).
Gna is in charge of the hosting of SVN repository, mailing lists and trackers; while TuxFamily is in charge of website and downloads hosting.

In 2012, project source code is switched to Git ; and repositories are moved to Tuxfamily. Gna! tracker is abandoned as well.

At the begining of 2017, mailing lists are also switched to Tuxfamily, since Gna has announced the end of their services.

### Original Email

This is the **original email** (in french) which anounce Galette creation. Since then, the Code mailing-list from [ALDIL](https://www.aldil.org) has disappeared, archives too.
Also, first wiki website as disappeared too.

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

### From where Galette's name come?

[ALDIL](https://www.aldil.org/) members have long sought a name for this software. Here's a quick summary (in frenglish):

You must know that finally, Deelight (Lead developer: One who's right) choose Galette, GruiicK (President: One who said banco) said banco.

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
  LUGDUNUM : LUG Data User NUmeric Manager (also the latin name of Lyon),
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

(sorry, not translated, in french)

(fortunes from mail/irc/etc, anti-chronologeek order)

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
&lt;hertay&gt; Trashy, dans https://galette.eu c'est toujours la 0755 qui est en téléchargement (lien) ;-)
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

## Used tools

Managing a project like Galette requires that a certain number of technical solutions be implemented: [communication medium]({% tl contact %}), [source code web hosting](https://git.tuxfamily.org/galette/), [issues]({{ site.galette.tracker_url }}), ... Here's whhat's used:

* [source code](https://git.tuxfamily.org/galette/): [Git](https://git-scm.com/), hosted by [TuxFamily](https://tuxfamily.org),
* web site: built by [Jekyll](https://jekyllrb.com)[^1], webhosted by TuxFamily,
* [issues system]({{ site.galette.tracker_url }}) : [Redmine](https://redmine.org)[^2], hosted on a dedicated server,
* [démo](https://demo.galette.eu) : [Galette](https://galette.eu), hosted on a dedicated server,
* [discussion and broadcast lists]({% tl contact %}#listes-de-discussion) : [VHFFS](https://vhffs.org)[^3], provided by TuxFamily,
* [voting system]({{ site.galette.vote_url }}) : [Fider](https://fider.io), hosted by Fider,
* [documentation]({{ site.galette.doc_url }}/{{ site.lang }}/master) : built by [Sphinx](https://www.sphinx-doc.org)[^4], hosted by [ReadTheDocs](https://rtfd.org),
* [translations]({{ site.galette.trad_url }}) : [Weblate](https://weblate.org)[^5], hosted by Weblate.
* [documentation translation](https://translate.zanata.org/project/view/galettedoc/) : [Zanata](http://zanata.org)[^6], hosted by Zanata.
* Johan, hosted by himself :p

Although not being a free tool, [Galette has an official mirror on GitHub](https://github.com/galette), for multiple reasons:

* space is limited at TuxFamily. By using GitHub for developement branches, we avoid unnecessarily enlargement of our main repository,
* many have a GitHub account, not much a TuxFamily one,
* suggest a modification is more easy for users,
* revue system is handy,
* no need to manage on more system (as the actual list is already endless),
* continuous integration is there (tests are run each commit),
* code navigation is more easy than on TuxFamily,
* there's no git hooks at TuxFamily, and that's used for translation and documentation updates, and for test runs.

[^1]: from 2020. Web site was using [Dotclear](https://dotclear.org) from 2012 to 2020, by [dokuwiki](https://dokuwiki.org) before 2012.
[^2]: from 2012. Before that, Gna! system was used.
[^3]: from 2017. Before that, lists were handled by [Mailman](https://list.org/) at Gna! until closure.
[^4]: from 2012. Everything was on the main web site before.
[^5]: from 2019. Translations were manually handled before.
[^6]: from 2019. Only French documentation was available.
