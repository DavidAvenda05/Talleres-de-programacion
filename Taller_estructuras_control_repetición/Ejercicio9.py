alc=0
gas=0
die=0

while True:
    ele=int(input())
    if ele==1:
        alc=alc+1
    elif ele==2:
        gas=gas+1
    elif ele==3:
        die=die+1
    elif ele==4:
        break
print("Muito Obrigado")
print(f"Preferencia de Gasolina:{gas}")
print (f"Prefencia Alcohol: {alc}")
print(f"Preferencia Diesel: {die}")