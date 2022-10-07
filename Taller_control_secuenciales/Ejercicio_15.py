pvp=float(input("precio de venta al publico: "))
pfp=float(input("precio de compra final: "))
#caja negra
d=(pvp-pfp)
desc=round(((d/pvp)*100),3)
#salida
print("el descuento que se aplico al precio de venta es: "+str(desc))
