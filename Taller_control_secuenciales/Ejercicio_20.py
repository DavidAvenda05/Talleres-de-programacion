pc=float(input("introducir el precio por computador: "))
p_cuotas=float(input("introducir el valor por cuota: "))
#caja negra
p=p_cuotas-(pc/12)
interes=(p*100)/p_cuotas
i1=round(interes,2)
#salida
print(f"El porcentaje del combro por pago en cuotas {i1} %")