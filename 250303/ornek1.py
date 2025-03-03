bagaj=int(input("bagajın kgsini gir"))
if bagaj <=20:
    print("herhangi bir ücret ödemeniz gerekmez")
else:
    fark=bagaj-20
    print("fazla bagaj için", 10 *fark,"tl ücret ödemeniz gerekir")
print("iyi yolculuklar")