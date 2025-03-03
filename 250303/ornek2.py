urun1=int(input("ürünün fiyatını girin"))
urun2=int(input("ürünün fiyatını girin"))
toplam=(urun1+urun2)
if toplam<=200:
    print("ödenecek miktar",toplam)
else:
    odeme=toplam*0.75
    print("ödenecek miktar",odeme)