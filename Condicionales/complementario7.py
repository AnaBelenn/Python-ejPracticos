'''
Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto 
deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
'''
compra=float(input("Ingrese el total de la compra: \n"))
if compra > 1000:
    print(f"Recibio un descuento del 15% que equivale a un total de ${compra*0.15}.\n- Monto final a pagar: ${compra-compra*0.15}")
else:
    print(f"No recibe ningun descuento. Monto final a pagar: ${compra}")