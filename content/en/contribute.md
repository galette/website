---
title: "Contribute"
description: "No need to be a developer to contribute to Galette: test it and report bugs, help other users, spread the word, translate, write documentation, write code or donate."
---
<p class="lead">Galette is free software, kept alive by its community. You don't need to be a developer to take part: a few minutes are often enough to make a real difference.</p>

{{< donate >}}

## Pick your way to help

{{< cards >}}
{{< card icon="bug" title="Test" anchor="test" meta="A few minutes · no technical skills" url="https://bugs.galette.eu/projects/galette/" button="Report a bug" >}}
Using Galette? A well-described bug report is already a valuable contribution.
{{< /card >}}
{{< card icon="help" title="Help" anchor="help" meta="Now and then · know Galette" url="https://github.com/orgs/galette/discussions" button="Answer questions" >}}
Share what you know with people who are discovering Galette.
{{< /card >}}
{{< card icon="share" title="Spread the word" anchor="spread-the-word" meta="A few minutes · no prerequisite" url="https://framapiaf.org/@galette" button="Follow Galette" >}}
Talk about Galette around you: other associations probably need it too.
{{< /card >}}
{{< card icon="translate" title="Translate" anchor="translate" meta="At your own pace · read English" url="https://hosted.weblate.org/projects/galette/" button="Translate on Weblate" >}}
Galette speaks about twenty languages thanks to volunteers. Why not yours?
{{< /card >}}
{{< card icon="write" title="Document" anchor="document" meta="At your own pace · plain English" url="https://doc.galette.eu/en/master/" button="Read the manual" >}}
The user manual is best written by people who use Galette every day.
{{< /card >}}
{{< card icon="code" title="Code" anchor="code" meta="Project · PHP, JavaScript" url="https://github.com/galette" button="Browse the code" >}}
Fix a bug, improve a plugin or propose a new feature.
{{< /card >}}
{{< /cards >}}

## Test and report bugs {#test}

Using Galette is already a way to support the project. If you run into a bug, open a ticket on the [bug tracker]({{% param "galette_tracker_url" %}}) with as many details as you can (version, steps to reproduce, error message): that is what gets it fixed quickly. Check first that nobody reported it before you.

Want to go further? Try the [nightly build]({{% param "galette_nightly_url" %}}), which contains the features under development, or the {{< doclink path="plugins/" >}}official plugins{{< /doclink >}}. The nightly build is unstable: test it on a copy of your data, never in production.

## Help other users {#help}

Know Galette well? Answer questions on [GitHub Discussions]({{% param "galette_discussions_url" %}}), in the [chat rooms]({{< ref "contact#instant-messaging" >}}) (Matrix, Discord, IRC) or on the [users mailing list]({{< ref "contact#mailing-lists" >}}). Helping a neighbouring association install or get started with Galette counts too.

Know a place where people help each other with Galette that is missing from the [contact page]({{< ref "contact" >}})? Let us know.

## Spread the word {#spread-the-word}

Talk about Galette on your social networks, at your LUG, at a meeting between associations or at an event. Share release announcements and follow the project on [social networks]({{< ref "contact#social-networks" >}}).

## Translate {#translate}

Galette, its documentation and the official plugins are translated on [Weblate](https://hosted.weblate.org/projects/galette/): create an account, pick your language and translate right in your browser. Your translations ship with the next releases.

The source language is English: if you spot a mistake in the English text itself, report it instead of working around it in a translation.

{{< img_link path="/site/assets/images/screenshots/weblate.png" alt="Translation platform Weblate screenshot" >}}

## Write documentation {#document}

Some features are barely described, or not at all, in {{< doclink path="" >}}the documentation{{< /doclink >}}, especially in the user manual, which is best written by users. No need for long texts or perfect English: original content is in English, but we can help with that, and every contribution is reviewed.

You don't need to know the documentation format either: propose your text on the [bug tracker](https://bugs.galette.eu/projects/documentation-galette) or on [GitHub Discussions]({{% param "galette_discussions_url" %}}), and we will take care of the formatting. If you know Git, a [pull request](https://github.com/galette/galettedoc) is welcome.

## Write code {#code}

Before you start, come and talk about it on the [communication channels]({{< ref "contact" >}}) or on [GitHub Discussions]({{% param "galette_discussions_url" %}}): you will know whether the feature fits in Galette and how to approach it. Plugins, often quite simple, are a good starting point, but contributions to the core are just as welcome.

The code of Galette, its plugins, documentation and website lives on [GitHub](https://github.com/galette), where pull requests are reviewed by the team. Everything you need to get started is in the {{< doclink path="source_code.html" branch="develop" >}}source code documentation{{< /doclink >}}.

## Make a donation {#donate}

Galette is free, with no paid edition and no ads. Donations pay for the time spent developing and maintaining it, for hardware, and for hosting the project services (demo, nightly builds, mailing lists).

* [Donate by card]({{% param "donate_stripe_url" %}}) through Stripe (transaction fees apply)
* for a bank transfer, a check or any other way, [get in touch]({{< ref "contact" >}})

Thank you for your support!
