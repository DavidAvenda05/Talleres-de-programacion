#entradas
act=float(input("introducir lectura del consumo actual: "))
ant=float(input("introducir lectura del consumo anteior: "))
#caja negra
lectura=(act-ant)

if (lectura>0 and lectura<100):
    kwh1=lectura*4600
    print("el precio a pagar son: ", kwh1)
elif (lectura>=101 and lectura<300):
    kwh2=lectura*80.00
    print("el precio a pagar son: ", kwh2)
elif (lectura>=301 and lectura<500):
    kwh3=lectura*100000
    print("el precio a pagar es: ", kwh3)
elif (lectura>=501):
    kwh4=lectura*120000
    print("el precio a pagar son: ", kwh4)