#entrada
n1=float(input("ingrese nota 1: "))
n2=float(input("ingrese nota 2: "))
n3=float(input("ingrese nota 3: "))
p1=float(input("ingresar nota del parcial: "))
t1=float(input("ingresar nota del trabajo final: "))
#caja negra
N_f=((((n1+n2+n3)/3)*0.55)+(p1*0.30)+(t1*0.15))
#salida
print("la nota final de computación es: "+str(N_f))