class Account:
    def __init__(self, isim, numara, bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print("isim: ", self.isim)
        print("numara : ", self.numara)
        print("Bakiye: ", self.bakiye)

    def paraCek(self,miktar):
        if(self.bakiye-miktar<0):
            print("Bakiyeniz yeterli degil")
        else:
            self.bakiye-=miktar
            print("Yeni Bakiye",self.bakiye)

    def paraYatir(self,miktar):
            self.bakiye +=miktar
            print("Yeni Bakiye",self.bakiye)

account = Account("davut",123,1234)
account.hesapBilgileri()
account.paraCek(50)
account.paraYatir(16)
