nombres=[]
notas=[]
est=0
rep=0
apr=0
i=1

for i in range(1, 10+1):
    nombre=str(input("Ingrese el nombre del estudiante: "))
    nota=int(input("Ingrese nota del estudiante: "))
    nombres.append(nombre)
    notas.append(nota)
    est=est+nota
    if nota<60:
        rep=rep+1
    else:
        apr=apr+1

estudiantes= {
    "1":{
    "nombre_estudiante": f"{nombres[0]}",
    "nota_estudiante": f"{notas[0]}"
    },
    "2":{

    "nombre_estudiante": f"{nombres[1]}",
    "nota_estudiante": f"{notas[1]}"
    },
    "3":{

    "nombre_estudiante": f"{nombres[2]}",
    "nota_estudiante": f"{notas[2]}"
    },
    "4":{

    "nombre_estudiante": f"{nombres[3]}",
    "nota_estudiante": f"{notas[3]}"
    },
    "5":{

    "nombre_estudiante": f"{nombres[4]}",
    "nota_estudiante": f"{notas[4]}"
    },
    "6":{

    "nombre_estudiante": f"{nombres[5]}",
    "nota_estudiante": f"{notas[5]}"
    },
        "7":{

    "nombre_estudiante": f"{nombres[6]}",
    "nota_estudiante": f"{notas[6]}"
    },
        "8":{

    "nombre_estudiante": f"{nombres[7]}",
    "nota_estudiante": f"{notas[7]}"
    },
        "9":{

    "nombre_estudiante": f"{nombres[8]}",
    "nota_estudiante": f"{notas[8]}"
    },
        "10":{

    "nombre_estudiante": f"{nombres[9]}",
    "nota_estudiante": f"{notas[9]}"
    }
}

promedio=est/10

print("La cantidad de estudiantes aprobados es: ", apr)
print("La cantidad de estudiantes reprobados es: ", rep)
print("el promedio de notas del salon es: ", promedio)
