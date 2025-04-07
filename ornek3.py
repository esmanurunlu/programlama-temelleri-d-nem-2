kadi=input("kullanıcı adı girin :")
karakter_sayi= len(kadi)
 
if karakter_sayi == 0:
    print("boş geçilmez")
elif karakter_sayi>0 and karakter_sayi <3:
    print("kullanıcı adıdı çok kısa")
elif karakter_sayi>=3 and karakter_sayi <=9:
    print("kullanıcı adı uygun")
else:
    print("kullanıcı adı çok uzun")