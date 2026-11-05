À cette étape, nous exécutons les commandes suivantes :

- `ls -la`
- `find / -user flag01 2>/dev/null` 

Cependant, ces commandes ne nous permettent pas d'obtenir de résultat exploitable.

Nous consultons ensuite le fichier `/etc/passwd`, car il contient les informations relatives aux utilisateurs du système.

Autrefois, les mots de passe sous forme de hash étaient stockés directement dans ce fichier. 
Aujourd'hui, ils sont stockés dans `/etc/shadow`, un fichier dont l'accès est restreint pour des raisons de sécurité.

`cat /etc/passwd`
### Un point important pour l'analyse

Sous Linux, chaque ligne du fichier `/etc/passwd` contient généralement 7 champs séparés par le caractère `:` :
username:password:UID:GID:comment:home_directory:shell

Si, dans le deuxième champ, on trouve une valeur chiffrée à la place de `x`, il faut vérifier s'il s'agit d'un hash de mot de passe (Password Hash).



Ici, nous constatons que l'utilisateur `flag01` possède un mot de passe sous forme de hash.

Lors du level00 , nous avons utilisé **John the Ripper**. Nous allons donc essayer de l'utiliser à nouveau pour voir s'il est capable de retrouver le mot de passe.

Pour cela :

1. Nous créons un fichier nommé `flag01.txt` dans `/var/tmp`. `echo "ciphertext" > /var/tmp/flag01.txt`
2. Nous copions ce fichier sur la machine hôte, dans le répertoire `run` où John the Ripper est installé.
3. Nous lançons John the Ripper en lui indiquant le fichier `flag01.txt`.
4. Nous vérifions s'il parvient à retrouver le mot de passe à partir du hash.

L'objectif est de voir si John the Ripper peut casser ce hash et retrouver le mot de passe correspondant.


Nous exécutons John the Ripper sur la machine hôte, depuis le répertoire `run`, à l'aide de la commande suivante :

./john path-to-file

Sans utiliser l'option `--show`, John the Ripper affiche le type d'algorithme de hachage utilisé ainsi que le mot de passe qu'il a réussi à retrouver.

su flag01 --- password ---- getflag ---- su level02 ----- token