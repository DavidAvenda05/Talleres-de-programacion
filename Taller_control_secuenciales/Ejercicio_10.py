#entradas 
aus=float(input("introducir valor en chelines austriacos: "))
gre=float(input("introducir valor en dracmas griegos: "))
esp=float(input("introducir valor en pesetas: "))
#caja negra 
c1=float(aus*956871)/100
c2=float((gre*88607)/100)/20110
c3=float(esp/122499)
c4=float(esp*100)/9289
#salidas
print(f"la conversión de {aus} a pesetas es:  {c1} pesetas")
print(f"la conversión de {gre} a francos franceses es: {c2} francos franceses")
print(f"la conversión de {esp} a dolares es: {c3} dolares")
print(f"la conversión de {esp} a liras italianas es: {c4} liras italianas")
