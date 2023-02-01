#lkm

# summa > 0
# toista lkm kertaa
    #heitä noppaa, päivitä summa

# tulosta summa

import random

lkm = int(input('Anna noppien lukumäärä: '))

summa = 0
for luku in range(lkm):
    #heitä noppaa, tallenna tulos muuttujaan summa
    summa += random.randint(1,6)

    print(summa)