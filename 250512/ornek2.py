liste=[]
toplam=0

for i in range(8):
    liste.append(int(input("bir sayı girin: ")))

for sayi in liste:
    if  liste %2==0:
        toplam=toplam+sayi
print("toplam",toplam)