sure=int(input("süreyi girin"))
if sure<=60:
    print("ücret:5tl")
elif sure <=300:
    print("ücret:"+str((sure/60)*4+))
else:
    print("ücret:"+str((sure/60)*3)+"TL")