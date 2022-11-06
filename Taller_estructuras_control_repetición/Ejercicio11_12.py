personas=[]
consume=[]
licor=[]
edad=[]
sexo=[]
encuestados=int(input("Número de personas encuestadas: "))
e=0
i=0
contSi=0
sm=0
sf=0
mayor=0
menor=0
while (i<encuestados):
    e=i+1
    encuestados.append(e)
    cons=str(input("Consume licor?"))
    consume.append(cons)
    if (cons==("no")):
        eda=int(input("introducir edad: "))
        edad.append(eda)
        if eda>=18:
            mayor=mayor+1
        if eda<18:
            menor=menor+1
        sex=str(input("Sexo: "))
        sexo.append(sex)
        if sex=="M":
            sm=sm+1
        if sex=="F":
            sf=sf+1
        if (cons=="si"):
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
        if sex== "M":
            sm=sm+1
        if sex== "F":
            sf=sf+1  
    i=i+1

print(f"El total de consumidores es de: {contSi}")
print(f"El total de mujeres menores de edad es de {sf-mayorde}")
