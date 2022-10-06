n_h=int(input("introduzca el numero de hombres en la clase: "))
n_m=int(input("introuzca el numero de mujeres en la clase: "))
#caja negra
n_e=(n_h+n_m)
p_h=((n_h*100)/n_e)
p_m=((n_m*100)/n_e)
#salida
print("El porcentaje de mujeres es: ",p_m)
print("El porcentaje de hombres es: ",p_h)

