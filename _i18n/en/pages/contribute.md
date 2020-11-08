You would like to contribute, but you do not know what to do? Maybe do you think you cannot do nothing at all...

Don't panic, there are numerous ways to contribute to a project like Galette, no need to be a developer ;-)

## Use / Test

Using Galette is already a kind of support. Quite easy, no? Well, thanks for coming :D

For the ones who stay anyway, using and testing Galette is the same process. So, if you find a bug, open a ticket with all possible details so a developer can understand the issue and reproduce it, or use [one of our communication channels]({% tl contact %}) to expose your issue.

If you want - especially now you are a Galette expert! - you can test new features under development when there are, or regularly try the [nightly version]({{ site.galette.nightly_url }}). Do not forget this is an unstable version; even if instability is a relative concept.

Of course, this is the same for [official plugins]({{ site.galette.doc_url }}/{{ site.lang }}/master/plugins/) :-)

## Help / Communicate

Another possible way to contribute to the project is to help to install, configure or take in hand the tool.

That can be for your neighbour's association to which Galette can be helpful, or if he cannot achieve to install it, for example.
But that can also be a answering a question on the mailing lists or any other communication channel. By the way, if you know Galette help channels that are not listed in our contact page, please give us an highlight so we can add it.

To communicate about Galette is also a good way to contribute, and does not require any specific skills. Talk about Galette on your social networks ([Galette ones]({% tl contact%}#social-networks) are listed on contact page), during your LUG meetings or else.

<a name="donate"></a>
## Make a donation

Another way to contribute is to give the main Galette developer, Johan, a donation; trying to motivate him a bit ;-)

So you can:

* participate to the [current Galette pool](https://paypal.me/pools/c/8u4dEPpM0q) on PayPal[^1],
* contact him for any other payment method (transfer, check, possible other platform, ...)
* make a [PayPal donation](https://www.paypal.me/galettesoft)[^2] (last resort, if possible)

[^1]: Free of charge
[^2]: Some fees are applied (about 1 euro for a 25 donation)

## Translate

Preamble. All contribution to the project must be done in the main language (`en_GB` english). In case of mistake in the main language, it must get fixed in the original contents (source code).
Do not hesitate to use provided [contact channels ]({% tl contact %}) to find help about that if you need ;-)

So, if you want to help translating Galette, that is quite simple: go to the [translation platform (Weblate)](https://hosted.weblate.org/projects/galette/galette/), create or link an account if needed, login and translate!

{% responsive_image path: assets/images/screenshots/weblate.png alt: "Weblate interface" title: "Weblate interface" %}

For the documentation, this is the same with the difference that translations are done on the old [translation platform (Zanata)](https://translate.zanata.org/project/view/galettedoc/) (similar platform as Weblate or Transifex; but ageing).

{% responsive_image path: assets/images/screenshots/zanata.png alt: "Zanata interface" title: "Zanata interface" %}

And finally plugins... None of them use currently any external translation system. Process requires tools and editors on the user work station, when just a browser is enough for Galette or its documentation.

### Process details

If we take Galette example, new strings are regularly added to the source code. From time to time, strings are extracted from source code (and English updated de facto, nothing should differ between source code and English translation).
This operation ends in a commit on the source code repository, that will be automatically detected from translation system once pushed. All languages files are then automatically updated.

Once the language files has been updated, you can translate in the language that you choose. Applied changes are stored on the system, until developers pull them back in the soft repository (manual step). All translations are then available from Galette!

Except for plugins, there is no need to understand [internationalisation in Galette](https://translate.zanata.org/project/view/galettedoc/) to help translating, but the paragraph on lang files generation gives maybe a few technical precisions.

## Write

Some Galette features are missing from documentation (or have very few details). Here also, you can help writing documentation, or publications for the website. Most of the misses are in the user manual; section that should precisely be written from users (more often, developers give too much technical details).

The main constraint is that original contents must be in English. The goal is not to write great texts, no need to be fully bilingual. And if you do not speak English at all, it is always possible to get help on that point.
Contributions are anyway always reviewed and commented if needed, allowing adjustments from you or another participant.

Of course, documentation must fit some technical constraints to be published, but this is not mandatory for new contents. If for example you do not know how to make a link, just drop a word in the contents, for example `see xyz article (https://xyz.com)`.

If you want to complete documentation or add a fix, the way to go is the same as Galette's one: you may use [communication channels]({% tl contact %}) to explain your issue, and in all cases open a bug or feature request on the [bug tracker](https://bugs.galette.eu/projects/documentation-galette), we will adapt according to each level and skills after that.

## Hack / fix

Before you begin to write code, make sure your feature would be accepted, as well as the implementation you want to go with. This is the goal of [different communication channels]({% tl contact %}), do not hesitate :)

We advice you to read the [Galette development documentation]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/) in order to get familiar with code and followed rules.

Dive in the code is the most technical contribution. Plugins will certainly be simplest to understand than Galette itself, most of them are quite simple; but you can of course propose change on the core :)
Anyway, try to ask with developer(s) who is certainly the more appropriate to help you on.

Source code of all projects (Galette, plugins, documentation, website) is hosted on Git repositories, any Git applicable patch of any method would be OK. If you do not know how to proceed, maybe could you take a look on the corresponding GitHub mirror, some of them are already used for experimental features to prevent mess on the main repository. In GitHub case, we will use a PR (Pull Request) that will be reviewed by the development team.

All [really useful information for Galette source code or plugins are available in development documentation]({{ site.galette.doc_url }}/{{ site.lang }}/develop/development/git.html).
