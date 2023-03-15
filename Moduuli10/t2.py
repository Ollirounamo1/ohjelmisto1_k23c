class Hissi:
    def __init__(self, alin_kerros, ylim_kerros):
        self.etaisyys_alhaalla = True
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylim_kerros = ylim_kerros

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros != kohdekerros:
            if self.etaisyys_alhaalla:
                self.kerros_ylös()
            else:
                self.kerros_alas()
        print(f"Hissi on kerroksessa {self.kerros}.")

    def kerros_ylös(self):
        if self.kerros < self.ylim_kerros:
            self.kerros += 1
        else:
            self.etaisyys_alhaalla = False
        print(f"Hissi on kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        else:
            self.etaisyys_alhaalla = True
        print(f"Hissi on kerroksessa {self.kerros}.")


class Talo:
    def __init__(self, alin_kerros, ylim_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            hissi = Hissi(alin_kerros, ylim_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_nro, kohdekerros):
        hissi = self.hissit[hissin_nro]
        hissi.siirry_kerrokseen(kohdekerros)


# testikoodi
talo = Talo(alin_kerros=1, ylim_kerros=10, hissien_lkm=2)
talo.aja_hissiä(hissin_nro=0, kohdekerros=5)
talo.aja_hissiä(hissin_nro=1, kohdekerros=8)
