lista=[]
n=int(input("introduzca el número de estudiantes: "))
i=1
while (n>0):
    N=str(input("ingrese nombre"))
    pf=str(input("puntaje final: "))
    tupla=(N,pf)
    lista.append(tupla)
    i=i+1
    n=n-1

