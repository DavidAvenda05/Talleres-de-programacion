edad=float(input("digite la edad (si son meses en decimal, ej: 0.1): "))
sexo=str(input("digite el sexo: "))
nh=float(input("digite el nivel de hemoglobina en sangre: "))
#caja negra
if (edad>0 and edad<0.1 and nh>=13 and nh<26):
    print("no tiene anemia")
elif (edad>0.1 and edad<0.6 and nh>=10 and nh<18):
    print("no tiene anemia")
elif (edad>0.6 and edad<1 and nh>=11 and nh<15):
    print("no tiene enamia")
elif(edad>1 and edad<=5 and nh>=11.5 and nh<15):
    print("no tiene anemia")
elif(edad>5 and edad<=10 and nh>=12.6 and nh<15.5):
    print("no tiene anemia")
elif(edad>10 and edad<=15 and nh>=13 and nh<15.5):
    print("no tiene anemia")
elif(edad>15 and sexo=="mujer" and nh>=12 and nh<16):
    print("no tiene anemia")
elif(edad>15 and sexo=="masculino" and nh>=14 and nh<18):
    print("no tiene anemia")
else:
    print("tiene anemia")

