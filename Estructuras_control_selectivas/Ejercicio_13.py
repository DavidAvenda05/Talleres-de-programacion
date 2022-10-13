#sacar el dia, mes y año de hoy
from datetime import datetime
hoy = datetime.now()
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#entradas
fecha_nacimiento=input("poner en formato dd/mm/yyyy: ")
(dia,mes,año)=fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#caja negra
#-----------------calcular edad---------------------
edad=0
if(mes_actual>mes_nacimiento):
    edad=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
print("la edad es: ", edad)
#--------------signo sodiacal-------------------
if (mes_nacimiento==11 and 22<=dia_nacimiento<=30 or mes_nacimiento==12 and dia_nacimiento<21):
    print("su signo sodiacal es sagitario")
elif(mes_nacimiento==12 and 22<=dia_nacimiento<=31 or mes_nacimiento==1 and dia_nacimiento<20):
    print("su signo sodiacal es capricornio")
elif(mes_nacimiento==1 and 21<=dia_nacimiento<=31 or mes_nacimiento==2 and dia_nacimiento<19):
    print("su signo sodiacal es acuario")
elif(mes_nacimiento==2 and 20<=dia_nacimiento<=28 or mes_nacimiento==3 and dia_nacimiento<19):
    print("su signo sodiacal es piscis")
elif(mes_nacimiento==3 and 21<=dia_nacimiento<=31 or mes_nacimiento==4 and dia_nacimiento<20):
    print("su signo sodiacal es aries")
elif(mes_nacimiento==4 and 21<=dia_nacimiento<=30 or mes_nacimiento==5 and dia_nacimiento<21):
    print("Su signo sodiacal es tauro")
elif(mes_nacimiento==5 and 22<=dia_nacimiento<=31 or mes_nacimiento==6 and dia_nacimiento<21):
    print("su signo sodiacal es geminis")
elif(mes_nacimiento==6 and 22<=dia_nacimiento<=30 or mes_nacimiento==7 and dia_nacimiento<22):
    print("su signo sodiacal es cancer")
elif(mes_nacimiento==7 and 23<=dia_nacimiento<=31 or mes_nacimiento==8 and dia_nacimiento<23):
    print("su signo sodiacal es leo")
elif(mes_nacimiento==8 and 24<=dia_nacimiento<=31 or mes_nacimiento==9 and dia_nacimiento<22):
    print("su signo sodiacal es virgo")
elif(mes_nacimiento==9 and 23<=dia_nacimiento<=30 or mes_nacimiento==10 and dia_nacimiento<22):
    print("su signo sodiacal es libra")
elif(mes_nacimiento==10 and 23<=dia_nacimiento<=31 or mes_nacimiento==11 and dia_nacimiento<21):
    print("su signo sodiacal es escorpion")

