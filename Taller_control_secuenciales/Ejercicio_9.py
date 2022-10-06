h=float(input("introducir numero de horas trabajadas: "))
p_h=float(input("introducir valor de hora trabajo: "))
#caja negra
s_b=float(h*p_h)
s_n=float(s_b)-(s_b*0.20)
#salida
print("el sueldo neto segun las horas trabajadas es: "+str(s_n))
