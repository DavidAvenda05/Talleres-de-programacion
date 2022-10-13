km=float(input("introduzca los kilometros recorridos: "))
#caja negra
if(km<300):
    print (f"el valor a cancelar son $50000")
elif(km>300 and km<1000):
    pago=(70000+(30000*km))
    print(f"el pago total del cliente es ${pago}")
elif(km>1000):
    pago1=(150000+(9000*km))
    print(f"el cliente debe pagar${pago1}")