m_t=float(input("introduzca monto total de compra: "))
#caje negra
if (m_t>5000000): 
    inv=(m_t*0.55)
    p_b=(m_t*0.30)
    p_f=(m_t*0.15)
    print(f"La empresa invierte ${inv} , pide un prestamo al banco de ${p_b} y pide un credito al fabricante de ${p_f}")
    interes=(p_f*0.20)
    print(f"los intereses que se cobran por el prestamo es: ")
    cobro_t=(m_t+interes)
    print("el cobro total con los intereses es: ", cobro_t)
else:
    inv1=(m_t*0.70)
    p_f1=(m_t*0.30)
    print(f"la empresa invierte ${inv1} y pide un credito al fabricante de ${p_f1}")
    interes1=(p_f1*0.20)
    print(f"los intereses que se cobran son ${interes1} ")
    cobro_t1=(m_t+interes1)
    print("el cobro total de las piezas es: ", cobro_t1)
