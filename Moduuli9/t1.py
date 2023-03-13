class Auto:
    def __init__(self, rekisteri_tunnus, huippunopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.auton_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteri_tunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Auton nopeus:", auto.auton_nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")

