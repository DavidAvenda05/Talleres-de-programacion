COP=float(input("Ingrese la cantidad en pesos: "))
#caja negra
if (COP>100000):
    print((COP//100000), "billetes de 100000")
if (COP>=50000<100000):
    print(((COP%100000)//50000), "billetes de 50000")
if (COP>=20000<50000):
    print((COP%50000/20000), "billetes de 20000")
if (COP>=10000<20000):
    print((COP%20000//10000), "billetes de 10000")
if (COP>=5000<10000):
    print((COP%10000//5000), "billetes de 5000")
if (COP>=2000<5000):
    print((COP%5000//2000), " billetes de 2.000 pesos")
if (COP>=1000<2000):
    print(((COP%5000)//1000), " billetes de 1.000 pesos")
if (COP>=500<1000):
    print((COP%1000//500), " monedas de 500 pesos")
if (COP>=200<500):
    print(((COP%500)//200), " monedas de 200 pesos")
if (COP>=100<200):
    print((COP%200//100), " monedas de 100 pesos")
if COP>=50<100:
    print(((COP%100)//50), " monedas de 50 pesos")