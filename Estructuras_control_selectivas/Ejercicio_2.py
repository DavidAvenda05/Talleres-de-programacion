#entrada
salario=float(input("digitar su salario: "))
#caja negra
if(salario<900000):
    aum=(salario+(salario*0.15))
    sueldo_f=aum
elif(salario>=900000):
    aum_1=(salario+(salario*0.12))
    sueldo_f=aum_1
#salida
print(f"El sueldo despues del aumento es de ${sueldo_f}: ")
