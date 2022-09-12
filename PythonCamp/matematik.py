class Mathematik:
    def __init__(self, sayi1, sayi2):
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik basladi. Constracter yapici klass")

    def topla(self):
        return self.s1 + self.s2

    def cikar(self):
        return self.s1 - self.s2

    def bolme(self):
        return self.s1 / self.s2

    def carpma(self):
        return self.s1 * self.s2


mathematik = Mathematik(6, 3)
ergebnis = mathematik.topla()
print(ergebnis)

ergebnis = mathematik.cikar()
print(ergebnis)


class istatistik(Mathematik):
    def varyansHesapla(self):
        return self.s1 * self.s2


istatistik = istatistik(4, 5)
