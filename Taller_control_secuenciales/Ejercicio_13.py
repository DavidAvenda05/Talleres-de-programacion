b_50=int(input("cantidad de billetes de 50000: "))
b_20=int(input("cantidad de billetes de 20000: "))
b_10=int(input("cantidad de billetes de 10000: "))
b_5=int(input("cantidad de billetes de 5000: "))
b_2=int(input("cantidad de billetes de 2000: "))
b_1=int(input("cantidad de billetes de 1000: "))
m_500=int(input("cantidad de monedas de 500: "))
m_100=int(input("cantidad de monedas de 100: "))
#caja negra
d_t=((b_50*50000)+(b_20*20000)+(b_10*10000)+(b_5*5000)+(b_2*2000)+(b_1*1000)+(m_500*500)+(m_100*100))
#salida
print("la cantidad de dinero en el banco es: "+str(d_t))