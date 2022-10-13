#entrada
inv=float(input("Escriba el monto a invertir: "))
v_int=float(input("escriba el porcentaje de interes: "))
#caja negra
interes=(inv*(v_int/100))
Total=(inv+interes)
#caja negra
print("el total de dinero que generan los interes son: ", interes)
if (interes<100000):
    print("No reinvertir en el banco")
elif (interes>=100000):
    print("invertir nuevamente")
#salida
print(f"el monto total en su cuenta es de ${Total}")

