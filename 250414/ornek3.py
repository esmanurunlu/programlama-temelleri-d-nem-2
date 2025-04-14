kenar1=int(input(1.kenarı girin))
kenar2=int(input(2.kenarı girin))
kenar3=int(input(3.kenarı girin))
if kenar1==kenar2 and kenar2==kenar3:
    print("eşkenar üçgen")
elif kenar1==kenar2 or kenar2==kenar3 or kenar3==kenar1:
    print("ikiz kenaar üçgen")
else: 
    print("çeşit kenar üçgen")