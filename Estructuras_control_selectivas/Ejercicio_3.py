#entrada
A=int(input("introduzca valor A: "))
B=int(input("introduzca valor B: "))
C=int(input("introduzca valor C: "))
D=int(input("introduzca valor D: "))
#caja negra
if (D==0):
    x1=(A-C)**2
    print("el resultado es: ", x1)
elif (D>0): 
    x2=((A-B)**3)/D
    print("el resultado es: ", x2)