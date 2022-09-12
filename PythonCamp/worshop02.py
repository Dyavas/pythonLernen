sayi = int(input("Lutfen faktoriyel icin sayi giriniz: "))
faktoriyel = 1
if sayi == 0:
    print("Sayinin faktoriyeli: ", faktoriyel)
elif sayi < 0:
    print("Negatif sayilar hesaplanamaz")
else:
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i
        print("sonuc", faktoriyel)
