usuarios = { 
"iperurena": { 
"nombre": "Iñaki", 
"apellido": "Perurena", 
"password": "123123" 
}, 
"fmuguruza": { 
"nombre": "Fermín", 
"apellido": "Muguruza", 
"password": "654321" 
}, 
"aolaizola": { 
"nombre": "Aimar", 
"apellido": "Olaizola", 
"password": "123456" } 
} 
u= str(input("Introducir Usuario: "))
c= int(input("introducir contraseña: "))

if u in usuarios and c == usuarios[u]["password"]:
    print("Bienvenido: ", u)
else: 
    print("Usuario o contraseña incorrecta")
    