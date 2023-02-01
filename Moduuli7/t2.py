nimet = []

while True:
    nimi = input("Uusi nimi: ")
    if nimi == '':
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.append(nimi)

print("\nAnnetut nimet:")
for nimi in nimet:
    print(nimi)