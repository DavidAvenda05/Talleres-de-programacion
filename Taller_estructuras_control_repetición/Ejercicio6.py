n=int(input("Número entero: "))
k=int(input("Valor 2: "))
j=0
m=(n/k)
while (n>0):
    n=n-k
    j=j+1
    print(n)
print(f"Restas efectuadas {j}")
