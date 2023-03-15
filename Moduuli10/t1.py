class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif kohde_kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print("Hissi on kerroksessa", self.nykyinen_kerros)

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print("Hissi on kerroksessa", self.nykyinen_kerros)




h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

