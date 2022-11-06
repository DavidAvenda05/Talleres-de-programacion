#entradas
A=int(input("Introduzca valor de A "))
B=int(input("Introduzca valor de B "))
C=int(input("Introduzca valor de C "))
D=int(input("Introduzca valor de D "))
#caja negra
print(f"el numero entero es: {A}{B}{C}{D}")
if C>5 and B!=9:
    print(f"el numero redondeado es: {A}{B+1}00")
elif C>5 and B==9:
    print(f"el numero redondeado es: {A+1}000")
elif C<5:
    print(f"el numero redondeado es: {A}{B}00")

