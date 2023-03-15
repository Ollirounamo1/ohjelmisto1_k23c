import random



class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara

    def __str__(self):
        return f"{self.rekisteritunnus}: Nopeus: {self.nopeus} km/h, Huippunopeus: {self.huippunopeus} km/h, Matka: {self.kuljettu_matka} km"




#tee 10 autoa.
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)




kilpailu_jatkuu = True
while kilpailu_jatkuu:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False
            break




print("Kilpailun lopputulokset:")
for auto in autot:
    print(auto)
