Comme toujours, nous commençons par exécuter la commande `ls -la`.

On remarque ici la présence du caractère `s` dans les permissions, ce qui indique que le bit SetUID et/ou SetGID est activé.

Ensuite, nous examinons le fichier `level03`. Les informations affichées indiquent que le binaire n'est pas *strippé* (*not stripped*) et qu'il est exécutable.

Nous essayons de l'exécuter avec la commande :

./level03

Le message affiché pendant l'exécution nous indique qu'il existe probablement une faille dans le programme et que nous devons essayer de l'exploiter.

Puisque le fichier n'est pas *strippé*, nous utilisons la commande `strings` pour examiner les chaînes de caractères présentes dans le binaire et identifier celles qui pourraient nous donner des indices.

Nous trouvons notamment les chaînes suivantes :

- `system`
- `env echo`
- Le message que nous avons vu lors de l'exécution du programme.

Nous pouvons donc émettre l'hypothèse que le programme fait appel à la fonction `system()` et qu'il utilise la commande `env` pour exécuter le programme `echo`, auquel il transmet le texte à afficher comme argument.

Nous pouvons également utiliser le site "https://dogbolt.org" pour décompiler un fichier binaire et 
obtenir une représentation du code en assembleur ou dans un langage de plus haut niveau, comme le C.


Nous allons créer un fichier nommé `echo` dans le répertoire `/var/tmp`, puis lui donner les permissions d'exécution.

À l'intérieur de ce fichier, nous allons mettre le chemin absolu vers `getflag`, afin que, lorsque le programme `env` cherchera à exécuter `echo`, il exécute notre faux programme à la place du véritable `echo`.

Ainsi, au lieu d'afficher le texte habituel, notre faux exécutable lancera `getflag` et nous permettra d'obtenir le token.


