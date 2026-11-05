s = 'ciphertext'

for n in range(1, 26):
    print(
        n,
        ''.join(
            chr((ord(c) - 97 + n) % 26 + 97)
            for c in s
        )
    )
# Caesar Cipher: 
#- `for c in s` → Parcourt chaque caractère de la chaîne (`c` = character), un par un.
#- `ord(c)` → Convertit le caractère en sa valeur numérique ASCII. Par exemple : `a = 97`, `b = 98` ... `z = 122`.
#- `-97` → Ramène la valeur dans l'intervalle de 0 à 25 (c'est-à-dire `a = 0`, `b = 1` ... `z = 25`). Cela facilite les calculs.
#- `+n` → Décale le caractère de `n` positions vers l'avant. C'est le principe de la rotation.
#- `%26` → Calcule le reste de la division par 26. Si on dépasse `z`, on revient au début de l'alphabet. C'est le principe du modulo.
#- `+97` → Ramène la valeur dans l'intervalle des codes ASCII réels des lettres (à partir de 97).
#- `chr(...)` → Convertit à nouveau le nombre en caractère. C'est l'opération inverse de `ord()`.
#- `''.join(...)` → Assemble tous les caractères transformés pour former une seule chaîne de caractères.
#- `print(n, ...)` → Affiche le nombre de positions de rotation (`n`) et le résultat correspondant.