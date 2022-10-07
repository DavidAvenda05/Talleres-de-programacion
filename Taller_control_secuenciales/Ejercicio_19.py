#entrada
x=int(input("cantidad de naranjas compradas: "))
y=float(input("precio al que vende la docena: "))
k=float(input("venta total: "))
#caja negra
v=(x/12)*y
v_t=(((k-y)*100)/v)
#salidas
print(f"obtuvo una ganancia de {v_t} %")
