cons=0
licor=0
edad=0
sexo=0
Lista=[cons,licor,edad,sexo]
i=0
e=0
i=0
contSi=0
sexoM=0
sexoF=0
mayorde=0
menorde=0
while (i):
    e=i+1
    Lista.append(e)
    consE=str(input("Consume licor? "))
    cons.append(consE)
    if (consE==("no")):
        edadE=int(input("Que edad tiene? "))
        edad.append(edadE)
        if edadE>18:
            mayorde=mayorde+1
        if edadE<18:
            menorde=menorde+1
        sexoE=str(input("Su sexo? "))
        sexo.append(sexoE)
        if sexoE == "M":
            sexoM=sexoM+1
        if sexoE == "F":
            sexoM=sexoF+1
        if (consE=="si"):
            contSi=contSi+1
            edadE=int(input("Que edad tiene? "))
            edad.append(edadE)
        if edadE>18:
            mayorde=mayorde+1
        if edadE<18:
            menorde=menorde+1
        bebidasE=int(input("Que tipo de licor le gusta? "))
        if bebidasE == 1:
            licor.append('Aguardiente')
        if bebidasE == 2:
            licor.append('Ron')
        if bebidasE == 3:
            licor.append('Cerveza')
        if bebidasE == 4:
            licor.append('Tequila')
        if bebidasE == 5:
            licor.append('Wisky')
        if bebidasE == 6:
            licor.append('Otros')         
        sexoE=str(input("Su sexo? "))
        sexo.append(sexoE) 
        if sexoE == "M":
            sexoM=sexoM+1
        if sexoE == "F":
            sexoM=sexoF+1  
    i=i+1

print(f"El total de consumidores es de: {contSi}")
print(f"El total de mujeres menores de edad es de {sexoF-mayorde}")