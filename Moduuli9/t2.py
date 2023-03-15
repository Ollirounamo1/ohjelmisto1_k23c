class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeusmuutos):
        uusi_nopeus = self.nopeus + nopeusmuutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def __str__(self):
        return f"Auto {self.rekisteritunnus}, nopeus {self.nopeus} km/h, kuljettu matka {self.kuljettu_matka} km"




auto = Auto("ABC-123", 142)
print(auto)



auto.kiihdyta(30)
print(auto)



auto.kiihdyta(70)
print(auto)



auto.kiihdyta(50)
print(auto)



auto.kiihdyta(-200)
print(auto)
