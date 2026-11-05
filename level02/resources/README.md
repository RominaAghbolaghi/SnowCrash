1) Nous exécutons la commande `ls -la` et trouvons un fichier au format PCAP.

En examinant ses permissions, nous constatons que nous avons uniquement le droit de le lire.

2) Nous exécutons ensuite la commande suivante :

file level02.pcap

Cette commande nous permet d'obtenir des informations sur le type de fichier.
Cette commande nous permet de confirmer que le fichier est binaire et qu'il s'agit bien d'un véritable fichier de capture réseau **TCPDump (PCAP)**.

`tcpdump` est un outil qui permet de lire et d'analyser les fichiers de capture réseau (PCAP).

Nous devons donc l'ouvrir avec un outil d'analyse réseau comme tcpdump, et non avec cat ou un éditeur de texte classique.



3) Nous exécutons la commande suivante pour vérifier s'il est installé sur le système :

which tcpdump

Si la commande retourne un chemin, par exemple :

/usr/sbin/tcpdump

Cela signifie que `tcpdump` est installé et que son exécutable est accessible via le `PATH` du système.

Si aucun chemin n'est retourné, cela peut signifier que `tcpdump` n'est pas installé ou que son répertoire n'est pas présent dans le `PATH`.


4) Ensuite, nous exécutons la commande suivante :

tcpdump -nn -A -r level02.pcap tcp
| Option | Fonction |
| `-nn` | Afficher les adresses IP et les ports sous forme numérique. |
| `-A` | Afficher le contenu des paquets au format ASCII. |
| `-r` | Lire les données à partir d'un fichier PCAP. |
| `tcp` | Filtrer les paquets TCP. |

Puis, nous recherchons des mots-clés.

Nous remarquons la présence des messages `login`, `password` et `Login incorrect`. Nous comprenons donc que l'utilisateur essaie de se connecter et saisit un mot de passe.

À partir du moment où le mot `password` apparaît, nous devons examiner attentivement les paquets suivants et essayer de filtrer les données envoyées par le client, dont la longueur (`length`) est supérieure à zéro.

****Le premier paquet toujours est envoyé du client vers le serveur.

5) Nous allons donc filtrer les paquets en utilisant l'adresse IP du client et les flags qui indiquent la présence de données.

Ensuite, nous examinons les paquets affichés, à partir du moment où le mot `password` apparaît et jusqu'au message `Login incorrect`.

C'est dans cet intervalle que se trouve probablement le mot de passe saisi par l'utilisateur.

tcpdump -nr level02.pcap -X 'src host client-IP and (tcp[tcpflags] & tcp-push != 0)'

la fin de chaque TCP Header est notre data, nous repérons ces données et les assemblons dans le bon ordre afin de reconstituer le mot de passe.



