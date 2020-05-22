There are numerous ways to contribute to a project like Galette. Here is a non exhaustive list:

* user support on [mailing lists]({% tl contact %}#mailing-lists) or, more rarely, on the [IRC channel]({% tl contact %}#irc),
* [translate](https://hosted.weblate.org/projects/galette/galette/) (Galette, but also documentation),
* [hack the code itself]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/index.html),
* write various documentations ([installation guide]({{ site.galette.doc_url }}/{{ site.lang }}/master/installation/index.html),[user guide]({{ site.galette.doc_url }}/{{ site.lang }}/develop/usermanual/index.html), [developer guide]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/index.html), [frequently asked questions]({{ site.galette.doc_url }}/{{ site.lang }}/develop/faq/index.html), ...),
* [hack, document and test plugins]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/index.html),
* test development versions,
* [make a donation to Galette's developer](https://www.paypal.me/galettesoft) (contact him if you prefer to use a check or a transfer),
* ...

If you want to participate to Galette, do not hesitate any longer!

There a a few things you've got to know about Galette before you begin... :)

## Galette's code

All [informations about Galette or plugins source code are available in the development documentation]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html).

### Test

Testing Galette's code is generally as simple as installing and using it :-) No specific knowledge is required.

Various contact methods are offered for you to get help or advices, trackers will permit you to report bugs, possibly ask for new functionnalities, and even to submit patches.

## Galette's documentation

Galette's documentation sourcecode is hosted on a GIT repository, [see documentation for more details]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html).

The documentation is written using [reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) format and built with [Sphinx](https://sphinx-doc.org/).

All these informations may seems a bit technical, but in reality, documentation is simply written in a bunch of text files with a specific syntax (really well documented) which looks like a wiki syntax; while offering many additionnal possibilities. There is no need for any particular knowledge here.

## Galette's website

Galette's website is powered by DotClear. [Galette's DotClear theme is available on a GIT repository](https://bitbucket.org/trashy/galette_dc_theme). If you fix something, I'll be happy to integrate it ;-)

## Translations

Translations in Galette are built on top of gettext and po files. There are various PO files editors; which let you find quickly new, fuzzy or missing strings. Part of [Galette's documentation is about internationalization]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/i18n.html), if you want to get more.

You may [help on translations](https://hosted.weblate.org/projects/galette/galette/) themselves from the translation platform!
