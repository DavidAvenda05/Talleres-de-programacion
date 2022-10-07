costo_k=float(input("insertar valor por kilovatio: "))
lec_ant=float(input("ingresar lectura anterior de consumo: "))
lec_act=float(input("ingresar lectura acutal de consumo: "))
#caja negra
pago_luz=((lec_act-lec_ant)*(costo_k))
#salida
print("el monto a pagar del recibo del agua es:"+str(pago_luz))
