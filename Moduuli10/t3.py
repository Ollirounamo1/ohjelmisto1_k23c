class Hissi:
    def __init__(self, alin_kerros, ylim_kerros):
        self.ulin = alin_kerros
        self.ylin = ylim_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
        print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.ulin:
            self.kerros -= 1
        print("Hissi on kerroksessa", self.kerros)

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin:
            kohde_kerros = self.ylin
        elif kohde_kerros < self.ulin:
            kohde_kerros = self.ulin

        while self.kerros < kohde_kerros:
            self.kerros_ylos()

        while self.kerros > kohde_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylim_kerros, hissi_lkm):
        self.hissit = [Hissi(alin_kerros, ylim_kerros) for _ in range(hissi_lkm)]

    def aja_hissia(self, hissin_nro, kohde_kerros):
        self.hissit[hissin_nro].siirry_kerrokseen(kohde_kerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].ulin)


talo = Talo(1, 10, 2)
talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.palohalytys()
