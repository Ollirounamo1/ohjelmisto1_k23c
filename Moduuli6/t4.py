#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen palauttaman summan.

def summa(kokonaisluvut):
    yhteensä = 0
    for x in kokonaisluvut:
        yhteensä += x
    return yhteensä
print(summa((9, 5, 3, 2, 7)))
