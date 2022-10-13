cat=int(input("introduzca la categoria del trabajador"))
#caja negra
if (cat==1):
    aum1=(5000000+(5000000*0.10))
    print(f"el sueldo del trabajador de categoria 1 es ${aum1}")
elif (cat==2):
    aum2=(4300000+(4300000*0.15))
    print(f"el sueldo del trabajador de categoria 2 es ${aum2}")
elif (cat==3):
    aum3=(3600000+(3600000*0.20))
    print(f"el sueldo del trabajador de categoria 3 es ${aum3}")
elif (cat==4):
    aum4=(2000000+(2000000*0.40))
    print(f"el sueldo del trabajador de categoria 4 es ${aum4}")
elif (cat==5):
    aum5=(900000+(900000*0.60))
    print(f"el sueldo del trabajador de categoria 5 es ${aum5}")
