toplam=0
s1=int(input("küçük olan sayıyı girin"))
s2=int(input("büyük olan sayıyı girin"))

for sayi in range(s1,s2):
    if sayi %2==0:
        toplam=toplam+sayi
print(s1,"ile",s2,"sayısının arasındaki çift sayiların toplam",toplam)