Puntaje=[]
Nombres=[]
cantidad=int(input("Introduzca la cantidad de estudiantes "))
i=0
sumatoria=0
promedio=0

while (i<cantidad):
    nombre=str(input("Indique el nombre del estudiante "))
    puntaje=float(input("Indique el puntaje del estudiante "))
    Nombres.append(nombre)
    Puntaje.append(puntaje)
    sumatoria=sumatoria+Puntaje[i]
    i=i+1
print(sumatoria)
promedio=sumatoria/cantidad
print(f"El promedio de las calificaciones es: {promedio}")
maximo=max(Puntaje)
minimo=min(Puntaje)
indiceMax=(Puntaje.index(maximo))
indiceMin=(Puntaje.index(minimo))
print(indiceMax)
print(indiceMin)
print(f"Nota mayor: {Nombres[indiceMax]}, con el puntaje de: {Puntaje[indiceMax]}")
print(f"Nota menor: {Nombres[indiceMin]}, con el puntaje de: {Puntaje[indiceMin]}")


