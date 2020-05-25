Vous vous demandez comment nous contacter ? Les moyens sont multiples ;-)

Et fonction du besoin :

* vous pouvez utiliser les canaux [IRC](#irc) et [Matrix](#matrix) pour absolument tous les sujets, ou même juste pour dire bonjour,
* vous pouvez également aborder tous les sujets sur les listes de diffusion, mais préférez la liste de développement pour les sujets liés au... développement,
* en cas de bogue ou de demande d'évolution, utilisez le gestionnaire de bogues (« bug tracker » en anglais, et « tracker » de son petit nom généralement utilisé),
* vous pouvez aussi proposer une nouvelle possibilité, si elle fait sens.

Sur les réseaux sociaux (Mastodon, Twitter), faire du support ou expliquer certaines choses, ça peut être compliqué... Nous préfèrerons privilégier un des autres canaux mis à disposition tant que faire se peut.

## Discussions instantanées

Posez une question, et obtenez une réponse. C'est simple, et efficace. Ça demande juste qu'il y ait quelqu'un en face pour vous répondre, et c'est là que ça se complique un peu :-D 

Il arrive parfois que les discussions instantanées ne le soient pas tant que ça, en fonction de chacun et du contexte... Le développeur principal est généralement toujours présent en pointillés.

### IRC

IRC est un protocole de communication qui existe depuis de nombreuses années (1988), qui fait très bien ce qu'on lui demande (pas grand chose somme toute), et qui est encore actuellement très répandu.

D'un côté, il existe de nombreux réseaux IRC, tels que [Freenode](https://freenode.net), [GIMPNet](https://www.gimp.org/) ou encore [OFTC](https://oftc.net). C'est ce dernier qu'utilise Galette. Sur chaque serveur, il existe de nombreuses salles ; celle de Galette se nomme `#galette`.

D'un autre côté il existe de très nombreux clients IRC, sur toutes les plates formes possibles à priori. Certains logiciels de messagerie instantanées permettent de aussi s'y connecter, tout comme Thunberbird. Le choix ne manque pas :-)

Tout ce dont vous avez besoin, c'est donc d'un client IRC pour vous connecter sur [irc.oftc.net](irc://irc.oftc.net) pour ensuite rejoindre `#galette`.

Notez que lorsque votre client IRC est fermé ou simplement non connecté, aucun message ne vous parviendra. Et vous ne pourrez jamais non plus voir ce que vous avez manqué (aucun log du canal IRC n'est disponible).

Récemment, un lien a été créé entre le salon IRC et l'instance Matrix ; qui devrait apporter une solution efficace à ce problème. En effet, c'est dans ce cas l'instance Matrix qui se connecte sur le canal IRC pour tous les participants.

### Matrix

Matrix est un protocole de communication bien plus récent, qui se veut ouvert et très interopérable. Le fonctionnement est un peu similaire à IRC, à la différence qu'il faut faudra d'abord un compte Matrix (sur quelque instance que ce soit[^1]), pour ensuite rejoindre le salon de Galette.

* salon Matrix : [#galette:matrix.org](https://matrix.to/#/#galette:matrix.org)
* et communauté : [+galette:matrix.org](https://matrix.to/#/+galette:matrix.org)

L'accès au salon est ouvert à tous, les archives ne sont pas publiques, vous n'aurez accès qu'aux conversations qui ont eu lieu après que vous ayez rejoint le salon.
Il est automatiquement lié au salon IRC officiel, vous n'avez rien de plus à faire.

[^1]: la connexion depuis un serveur tiers n'a pour le moment pas été confirmée, faites nous savoir si ça fonctionne ! ;-)

## Listes de discussion

Les listes de discussion sont un ensemble d'échanges par courriel. La liste est désignée par une adresse mail à laquelle vous envoyez un message, qui est ensuite redistribué à tous les abonnés de la liste (vous y-compris). Certaines listes de diffusion proposent de nombreuses options de configuration, comme la réception groupées ; mais ce n'est plus le cas désormais[^gna].

Afin d'envoyer ou de recevoir des messages d'une liste, vous devez **impérativement y être inscrit**. La procédure est expliquée sur la page de la liste elle-même et plus bas sur la présente page.

Les listes disponibles :

* [utilisateurs](https://listengine.tuxfamily.org/lists.galette.eu/users/) : discussions générales, entraide, FAQ
* [développement](https://listengine.tuxfamily.org/lists.galette.eu/devel) : liste de discussion développeurs pour les sujets plus techniques
* [commits](https://listengine.tuxfamily.org/lists.galette.eu/commits/) : diffusion des commits - *ceci n'est pas un liste de discussion*

Les archives des listes de 2004 à 2017 sont disponibles aux adresses suivantes :

* [utilisateurs](http://download.tuxfamily.org/galette/listes-galette/mail.gna.org/assets/images/galette-discussion/index.html),
* [développement](http://download.tuxfamily.org/galette/listes-galette/mail.gna.org/assets/images/galette-devel/index.html).

### Inscription/Désinscription et utilisation

Les listes de diffusion possèdent deux adresses différentes :

* l'adresse de la liste, <users@lists.galette.eu> par exemple, que vous utiliserez pour envoyer un message à la liste, et qui sera l'expéditeur des messages que vous recevrez,
* l'adresse administrative, composée du nom de la liste suivi de `-request`, <users-request@lists.galette.eu> par exemple, que vous utiliserez pour vous abonner ou vous désabonner.

Lorsque vous envoyez un courriel à l’adresse administrative de la liste pour vous abonner ou vous désabonner, vous devez recevoir un message de confirmation auquel vous devrez répondre pour que l'opération soit finalisée.

Si vous ne recevez pas ce message, ce n'est pas normal ; l'opération n'est pas terminée.

Vérifiez bien vos dossiers de spam, et ré-essayez[^buglist]. Si le problème persiste, essayez de [contacter directement TuxFamily](https://www.tuxfamily.org/fr/contact), ou contactez nous par un autre biais (nous contacterons TuxFamily :D).

Pour utiliser la liste, envoyez un message à son adresse principale, et c'est tout. Pour commencer une nouvelle conversation, il convient généralement de rédiger un nouveau courriel plutôt que de répondre à un message existant (changer le sujet ne trompe pas la liste ;)) ; il suffit juste de répondre sinon.

Lorsque vous envoyez un message sur a liste, vous devez le recevoir également. Si ce n'est pas le cas, ce n'est pas normal.

Si vous souhaitez [rechercher dans les archives des listes]({{ site.galette.doc_url }}/{{ site.lang }}/master/faq/index.html#how-to-search-in-lists-archives) voyez la FAQ.

[^gna]: jusque 2017, les listes de diffusion étaient gérées chez Gna! via GNU Mailman. Désormais, c'est géré chez TuxFamily via vhffs, qui propose moins d'options. Gna ayant définitivement fermé, il a fallu trouver une autre solution.
[^buglist]: récemment (mai 2020), un bogue qui bloquait les inscriptions et désinscriptions a été relevé et corrigé sur vhffs, les nouvelles tentatives suivantes étaient ignorées.

## Rapports de bogues et demandes d'évolutions

Des entrées de FAQ spécifiques traitent respectivement des procédures de [rapport d'anomalies et de demande d'évolution]({{ site.galette.doc_url }}/{{ site.lang }}/master/faq/index.html#how-to-report-a-bug-or-ask-for-a-feature).

Avant de [rapporter un bogue](https://bugs.galette.eu/projects/galette) ou [d'exprimer une demande de fonctionnalité](https://bugs.galette.eu/projects/galette/), assurez-vous que personne ne vous ait devancé :-)

* [liste des bogues ouverts](https://bugs.galette.eu/projects/galette/issues?query_id=2)
* [liste des tâches ouvertes](https://bugs.galette.eu/projects/galette/issues?query_id=3)
* [demandes soumises au vote](https://vote.galette.eu)

## Réseaux sociaux

* Twitter : [@galette_soft](https://twitter.com/galette_soft)
* Mastodon : [@galette@framapiaf.org](https://framapiaf.org/@galette)
* Salon Matrix : [#galette:matrix.org](https://matrix.to/#/#galette:matrix.org) et communauté : [+galette:matrix.org](https://matrix.to/#/+galette:matrix.org)
