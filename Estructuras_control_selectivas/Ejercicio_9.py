monto=float(input("introducir monto de la venta: "))
#caja negra
if (monto<50000):
    print("no hay descuento")
elif(monto>50000 and monto<=100000):
    desc=(monto-(monto*0.5))
    print(f"el descuento es del 5% y el monto a pagar es ${desc}")
elif(monto>100000 and monto<=700000):
    desc1=(monto-(monto*0.11))
    print(f"el descuento es del 11% y el monto a pagar es ${desc1}")
elif(monto>700000 and monto<=1500000):
    desc2=(monto-(monto*0.18))
    print(f"el descuento es del 18% y el monyo a pagar es ${desc2}")
elif(monto>1500000):
    desc3=(monto-(monto*0.25))
    print(f"el descuento es del 25% y el monto a pagar es ${desc3}")