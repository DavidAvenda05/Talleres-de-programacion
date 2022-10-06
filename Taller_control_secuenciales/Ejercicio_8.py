#entrada
import math
l1=float(input("introducir lado 1: "))
l2=float(input("introducir lado 2: "))
l3=float(input("introducir lado 3: "))
#caja negra
s=float((l1+l2+l3)/2)
a=float(math.sqrt(s*(s-l1)*(s-l2)*(s-l3)))
#salida
print("el area del triangulo es: "+str(a))
