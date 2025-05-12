ders_notları=[]
toplam=0
zayif_sayisi=0

for i in range (6):
    ders_notlari.append(int(input("ders notu girin:")))

for ders_notu in ders_notları:
    toplam=toplam+ders_notu
    if ders_notu<50:
        zayif_sayisi=zayif_sayisi +1

ortalama=toplam /6

print("ders notları ortalaması:",ortalama)
print("öğrencinin zayıf sayısı:",zayif_sayisi)