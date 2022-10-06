#entrada
sueldo_b=float(input("ingrese su sueldo base: "))
v_1=float(input("ingrese venta 1: "))
v_2=float(input("ingrese venta 2: "))
v_3=float(input("ingrese venta 3: "))
#caja negra
comisiones=((v_1+v_2+v_3)*0.10)
Sueldo_total=(comisiones+sueldo_b)
#salida
print("la comisión en ventas es: "+str(comisiones) , "su sueldo total es: "+str(Sueldo_total))

