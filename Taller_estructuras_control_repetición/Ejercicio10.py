altura=[] 
est=int(input("Número de estudiantes: "))
e=1
while (est>0):
    estatura = float(input(f"Estatura# {e}: "))
    altura.append(estatura)
    e=e+1
    est=est+1
    if est==e:
        break
    max=max(altura)
print(f"La altura mayor es: {max}")
print(f"Las estaturas son: {altura}")