import random


def heitä_noppaa():
    return random.randint(1,6)

while True:
    silmaluku = heitä_noppaa()
    print(silmaluku)
    if silmaluku == 6:
        break