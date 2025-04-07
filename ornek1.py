derece=int(input("derece girin"))
if derece <0:
    print("katı")
elif derece >=0 and derece < 100:
    print("sıvı")
else:
    print("gaz")