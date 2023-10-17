Want to know how to contact us? Ways are multiple ;-)

And depending on needs:

* you can use [IRC](#irc) and [Matrix](#matrix) channels for any subject, or just to say hello,
* you can also talk about everything on [mailing lists](#mailing-lists) but prefer development list to talk about... development,
* for a bug report or an enhancement request, use the bug tracker,
* you can also propose a new way, if that makes sense.

On social networks (Mastodon, Twitter), doing support or explain some things can be complicated... We prefer any other of the provided channels as much as possible.

## Instant messaging

Ask a question, and get an answer. It's simple and effective. It only requires someone in front to answer you, and this is where things may get a bit complicated :D

It may happen that instant messaging is not really instant, depending on every one and the context... Main developer is globally always present from time to time.

### IRC

IRC is a communication protocol that does exists from years (1988), which does well what we ask it (not much finally), and which is still widespread.

On one side, numerous IRC networks does exists, like [Freenode](https://freenode.net), [GIMPNet](https://www.gimp.org/) or [OFTC](https://oftc.net). This last one is used for Galette. On each server, there are numerous rooms; Galette one name is `#galette`.

On the other side, numerous IRC clients does exists, on all possible platforms as far as we know. Some other instant messaging software also permit to connect to IRC, like Thunderbird. There is no lack of choice :-)

All you need is an IRC client to connect to [irc.oftc.net](irc://irc.oftc.net) and then join `#galette`.

Note than when your IRC client is closed or just not connected, no message will be sent to you. And you will never be able to see what you've missed (no log of the IRC channel is available).

Recently, a bridge between IRC channel and Matrix room has been created; this should bring a solution to this problem. Indeed, this is the Matrix instance which connects to IRC in that case for all participants.

### Matrix

Matrix is a way more recent communication protocol, which aims to be open and interoperable. It operate almost like IRC, with the difference you will first have to create a Matrix account (on whatever instance[^1]), to join Galette discussion room.

* Matrix room: [#galette:matrix.org](https://matrix.to/#/#galette:matrix.org)
* and community: [+galette:matrix.org](https://matrix.to/#/+galette:matrix.org)

Room is accessible for everyone, archives are not public, you will just have access to the discussion which will happen after you've joined.
It is automatically linked to the official IRC channel, you do not have anything more to do.

[^1]: connecting from a third party server has not been confirmed yet, let us know if that works! ;-)

## Mailing lists

Mailing lists are a set of discussion by email. The list has an email address to which you can send message that are then delivered to all its subscribers (yourself included). Some mailing lists offers many configuration options, like grouped distribution; but this is no longer the case now[^gna].

In order to send or receive messages from the list, you **absolutely must be subscribed to it**. The process is explained on list page itself and below on this page.

Available lists:

* [users](https://listengine.tuxfamily.org/lists.galette.eu/users/): global discussions, help, FAQ
* [development](https://listengine.tuxfamily.org/lists.galette.eu/devel): developer mailing list for more technical subjects
* [translations](https://listengine.tuxfamily.org/galette.eu/translations/): discussions about translations only
* [commits](https://listengine.tuxfamily.org/lists.galette.eu/commits/) : commits broadcast - *this is not a mailing list*

Lists archives between 2004 and 2017 are available at:

* [users](http://download.tuxfamily.org/galette/listes-galette/mail.gna.org/assets/images/galette-discussion/index.html),
* [development](http://download.tuxfamily.org/galette/listes-galette/mail.gna.org/assets/images/galette-devel/index.html).

### Subscription/Unsubscription and usage

Mailing lists have two distinct email addresses:

* list address, <users@lists.galette.eu> as example, you will use to send a message to the list, and that will be the sender of the messages you will receive,
* administrative address, which is made up of list name followed by `-request`, <users-request@lists.galette.eu> as example, you will use **to subscribe or unsubscribe**. Action is defined in the email subject; this can be "subscribe", "unsubscribe" or "help" (do not add anything else in the subject).

Therefore, to [unsubscribe from the users mailing list](mailto:users-request@lists.galette.eu?subject=unsubscribe) just send an email with "unsubscribe" as subject (without quotes!) to administrative address.
To [subscribe to Galette users](mailto:users-request@lists.galette.eu?subject=subscribe), just replace "unsubscribe" in the object with "subscribe" :-)

When you send a message to the administrative address to subscribe or unsubscribe, you must have a confirmation message and you have to answer to it to finalize the operation.

If you do not receive that message, this is abnormal; operation is not finalized.

Double check you spam directories, and try again[^buglist]. If the problem remains, try to [contact TuxFamily directly](https://www.tuxfamily.org/fr/contact), or contact us from another method (we will contact TuxFamily :D).

To use the list, send a message to its main address, and that's all. To start a new discussion thread, please write a new email rather than answering to an existing one (changeing email subject does not mislead the list system ;)); just answer otherwise.

When you send a message to the list, you must receive it as well. If you do not, something is wrong.

If you want to [search into lists archives]({{ site.galette.doc_url }}/{{ site.lang }}/master/faq/index.html#how-to-search-in-lists-archives) please see the FAQ.

[^gna]: until 2017, mailing lists were hosted at Gna! with GNU Mailman. Now, it's at TuxFamily via vhffs, which propose lesser option. Gna is definitively closed, we had to find another solution.
[^buglist]: recently (may 2020), a bug that blocked subscription and unsubscription has been fixed on vhffs, all new attempts but the first one were ignored.

## Bugs reports and requests for enhancement

Specific FAQ entries are talking respectively about [bug reporting and asking for new features]({{ site.galette.doc_url }}/{{ site.lang }}/master/faq/index.html#how-to-report-a-bug-or-ask-for-a-feature).

Before [reporting a bug](https://bugs.galette.eu/projects/galette) or [ask for a new feature](https://bugs.galette.eu/projects/galette/), please make sure no one else already did :-)

* [opened bugs list](https://bugs.galette.eu/projects/galette/issues?query_id=2)
* [opened tasks list](https://bugs.galette.eu/projects/galette/issues?query_id=3)
* [requests submitted to vote](https://vote.galette.eu)

## Social networks

**Please do not ask for support on Twitter and Mastodon!**

* Twitter: [@galette_soft](https://twitter.com/galette_soft)
* Mastodon: [@galette@framapiaf.org](https://framapiaf.org/@galette)