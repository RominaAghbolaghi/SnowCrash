1) Avec `ls -la`, on ne trouve rien d'intéressant.

2) on utilise donc `find / -user flag00 2>/dev/null` pour rechercher tous les fichiers appartenant à l'utilisateur `flag00`, afin de voir s'il existe des fichiers qui pourraient nous fournir des informations utiles. 


Lorsque nous exécutons la commande :

level00@SnowCrash:~$ find / -user flag00 2>/dev/null

Nous obtenons les résultats suivants :

/usr/sbin/john
/rofs/usr/sbin/john

Ici, le nom `john` est déjà un indice pour nous. Nous expliquerons plus tard ce que signifie ce nom et pourquoi il est intéressant.

Pour connaître le type de ce fichier, nous utilisons la commande `file` :
level00@SnowCrash:~$  file /usr/sbin/john
/usr/sbin/john: ASCII text

Le résultat nous indique qu'il s'agit d'un fichier texte au format ASCII.

La prochaine étape consiste à vérifier ses permissions avec `ls -la` pour savoir si nous avons le droit de le lire :

level00@SnowCrash:~$ ls -la /usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /usr/sbin/john

Puisque nous avons les permissions nécessaires pour lire ce fichier comme auther, nous pouvons afficher son contenu avec la commande `cat` :

level00@SnowCrash:~$ cat /usr/sbin/john
plaintext/ciphertext

À ce stade, nous pouvons supposer que cette chaîne de caractères correspond au mot de passe du compte `flag00`.

Nous essayons donc de l'utiliser pour nous connecter à ce compte. Cependant, cela ne fonctionne pas.

level00@SnowCrash:~$ su flag00
Password: 
su: Authentication failure


Cela signifie que cette chaîne n'est probablement pas le mot de passe en clair (Plaintext). Elle pourrait avoir été chiffrée ou transformée à l'aide d'une autre méthode.

Nous devons donc poursuivre notre analyse afin de comprendre comment retrouver sa valeur originale.


Pour le mot de passe, comme il est composé uniquement de lettres, on suppose qu'il s'agit simplement d'une transformation du texte. On vérifie donc sur le site pour identifier le type de chiffrement utilisé.

**dCode** : Pour identifier le type de chiffrement ou d'encodage. https://www.dcode.fr

On teste le mot de passe obtenu pour user flag00, puis on exécute la commande `getflag` pour récupérer le token. apres on fait su level01 et son pass est le token optenu.