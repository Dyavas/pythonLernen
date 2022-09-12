#Sart bloklari uygulamada dallandirmak icin kullaniliriz.
# pytonda blok yapilari indentation ile ayarlanir bir tab lik bosluk
istenenKredi=100000
hesap=9555
minimumOlmasiGerekenHesap=10000

if hesap>=minimumOlmasiGerekenHesap:
    print("Kredi verilebilir")
    print("Odemeler hesaplandi.")
elif hesap>=9000 and hesap<=9500:
    print("müdürüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("Genel Mudure sorulacak")
else:
    print("Kredi almak icin bakiyeniz yeterli degil")
print("islem sonu")
