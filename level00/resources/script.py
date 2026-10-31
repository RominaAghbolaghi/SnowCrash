s = 'cdiiddwpgswtgt'

for n in range(1, 26):
    print(
        n,
        ''.join(
            chr((ord(c) - 97 + n) % 26 + 97)
            for c in s
        )
    )