import random


class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matka += self.nopeus

    def __str__(self):
        return f"{self.rekisteritunnus}: {self.matka:.1f} km"


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"\nKilpailun {self.nimi} tilanne:\n")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus}: nopeus {auto.nopeus} km/h, matka {auto.matka:.1f} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False




kilpailu = Kilpailu("Suuri romuralli", 8000, [Auto(f"ABC-{i}") for i in range(1, 11)])

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()


