sayi1=int(input("1.sayıyı girin"))
sayi2=int(input("2.sayıyı girin"))
islem=input("işlem seçin(+,-,*,/):")
if islem=="+":
   sonuc=sayi1+sayi2    
   print(sonuc)
elif islem=="-":
   sonuc=sayi1-sayi2
   print(sonuc)
elif islem=="*":
   sonuc=sayi1*sayi2 
   print(sonuc)
elif islem=="/":
   sonuc=sayi1/sayi2 
   print(sonuc)
else:
   print("yanlış işlem girdiniz")
