#entradas
nombre=str(input("insertar su nombre: "))
H_t=float(input("insertar numero de horas trabajadas: "))
pago_h=float(input("insertar pago por hora trabajada: "))
h_e=float(input("insertar número de horas extras trabajadas: "))
hijos=int(input("¿cuántos hijos tiene?"))
#caja negra
sueldo_b=(pago_h*H_t)
Deducciones=(sueldo_b)-(sueldo_b*0.14)
asignaciones=(250000+(173000*hijos)+180000)
pago_hx=(h_e)*(pago_h*0.25)
sueldo_n=(sueldo_b+asignaciones+pago_hx)-Deducciones
#salida
print(f"Hola {nombre}, su sueldo neto para el mes de diciembre es: {sueldo_n} COP")



