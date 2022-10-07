Bx=float(input("ingresar prestamo de dinero: "))
By=float(input("ingresar pago con impuestos (4años): "))
#caja negra
meses=(4*12)
i=(Bx*meses*By)/100
#salida
print("el interes que genera el prestamo es: ", meses)