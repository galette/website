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

{% include contents/foundation_mail.html %}

### From where Galette's name come?

[ALDIL](https://www.aldil.org/) members have long sought a name for this software. Here's a quick summary (in frenglish):

You must know that finally, Deelight (Lead developer: One who's right) choose Galette, GruiicK (President: One who said banco) said banco.

{% include contents/notthename.html %}

## Fortunes

(sorry, not translated, in french)

(fortunes from mail/irc/etc, anti-chronologeek order)

{% include contents/fortunes.html %}

## Used tools

Managing a project like Galette requires that a certain number of technical solutions be implemented: [communication medium]({% tl contact %}), [source code web hosting](https://git.tuxfamily.org/galette/), [issues]({{ site.galette.tracker_url }}), ... Here's what's used:

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

[^1]: from 2020. Web site was using [Dotclear](https://dotclear.org) from 2012 to 2020, and [dokuwiki](https://dokuwiki.org) before 2012.
[^2]: from 2012. Before that, Gna! system was used.
[^3]: from 2017. Before that, lists were handled by [Mailman](https://list.org/) at Gna! until closure.
[^4]: from 2012. Everything was on the main web site before.
[^5]: from 2019. Translations were manually handled before.
[^6]: from 2019. Only French documentation was available.
