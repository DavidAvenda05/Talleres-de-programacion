#entradas
sueldo=float(input("introduzca el sueldo neto de los trabajadores: "))
v_1=float(input("ventas del departamento 1: "))
v_2=float(input("ventas del departamento 2: "))
v_3=float(input("ventas del departamento 3: "))
#caja negra
vt=(v_1+v_2+v_3)
v_min=(vt*0.33)
extra=(sueldo+(sueldo*0.20))
if(v_1<v_min and v_2<v_min and v_3<v_min):
    print (f"los 3 departamentos no reciben el dinero extra por lo que su sueldo es ${sueldo}")
elif(v_1<v_min and v_2<v_min and v_3>v_min):
    print (f"el departamento tuvo las ventas minimas por lo que su sueldo es ${extra}")
elif(v_1<v_min and v_2>v_min and v_3>v_min): 
    print (f"Los departamentos 2 y 3 tuvieron las ventas minimas por lo que su sueldo es {extra}")
elif(v_1>v_min and v_2>v_min and v_3>v_min):
    print (f"los 3 departamentos 1, 2 y 3 tuvieron las ventas minimas por lo que el sueldo es ${extra}")
elif(v_1>v_min and v_2>v_min and v_3<v_min):
    print (f"los departamentos 1 y 2 tuvieron las ventas minimas por lo que su sueldo es ${extra}")
elif(v_1>v_min and v_2<v_min and v_3<v_min):
    print (f"el departamento 1 tuvo las ventas minimas por lo que su sueldo es ${extra}")
elif(v_1<v_min and v_2>v_min and v_3<v_min):
    print (f"el departamento 2 tuvo las ventas minimas por lo que su sueldo es ${extra}")
elif(v_1>v_min and v_2<v_min and v_3>v_min):
    print (f"los departamentos 1 y 3 tuvieron las ventas minimas por lo que su sueldo es ${extra}")
    