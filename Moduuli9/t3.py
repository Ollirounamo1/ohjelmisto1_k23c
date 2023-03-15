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
        matka = self.nopeus * tuntimaara
        self.kuljettu_matka += matka



auto = Auto("ABC-123", 142)


print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")



auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)


print("Nopeus:", auto.nopeus, "km/h")



print("Nopeus:", auto.nopeus, "km/h")



# Kuljetaan autolla yhden tunnin verran
auto.kulje(1)



# Tulostetaan kuljettu matka
print("Kuljettu matka:", auto.kuljettu_matka, "km")
