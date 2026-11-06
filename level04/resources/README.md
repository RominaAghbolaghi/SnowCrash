
On commence par exécuter la commande `ls -la` pour examiner les fichiers présents dans le répertoire `level04`.

On remarque la présence d'un fichier qui appartient à `flag04`. 

Les informations que nous obtenons sont les suivantes :

- Le fichier possède les permissions **SUID** et **SGID**.
- Pour le moment, nous nous intéressons particulièrement au **SUID**, qui est associé à l'utilisateur `flag04`.
- (file level04): Nous avons également un fichier Perl exécutable.

Comme ce fichier est un fichier texte ASCII, nous pouvons utiliser la commande `cat level04` pour lire son contenu.

Le contenu nous donne des informations concernant **CGI**, `localhost` et un port.

Cela nous indique qu'un serveur Web est probablement actif sur le système et qu'il exécute ce script Perl à travers CGI.

Cela nous rappelle que nous pouvons utiliser `curl` pour envoyer une requête HTTP au serveur et ainsi déclencher l'exécution de ce script Perl.

À l'intérieur du fichier, nous remarquons un appel à `print` ainsi que l'exécution de la commande `echo`, placée entre des **Backticks**.

En Perl, les Backticks permettent d'exécuter le contenu qu'ils encadrent comme une commande Shell. Le résultat de cette commande est ensuite récupéré par le programme.

Nous remarquons également que le script récupère une donnée sous forme de paramètre.

Cela nous rappelle que nous pouvons transmettre ce paramètre au script en envoyant une requête HTTP avec `curl`.



curl 'localhost:4747/level04.pl?x=`getflag`'
curl 'http://localhost:4747/?x=$(getflag)'
curl "http://localhost:4747/?x=hello%3Bgetflag"
curl "http://localhost:4747/?x=hello%26%26getflag"
curl "http://localhost:4747/?x=\`getflag\`"
curl "http://localhost:4747/?x=\$(getflag)"

