adet=int(input("kaç tane alacaksınız :"))
birim_fiyat=int(input("ürünün birim fiyatını girin:"))
toplam=adet*birim_fiyat
if toplam>=3000:
    toplam=toplam-toplam*0.20
    print("ürünün tutarı:",toplam)
else:
    toplam=toplam 100
    print("ürünün tutarı:",toplam)