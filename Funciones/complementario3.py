'''
Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95 para cada segundo elemento 
posterior. Escriba una función que tome el número de elementos en el pedido como su único parámetro. Devuelva los gastos de envío del 
pedido como resultado de la función. Incluya un programa principal que lea la cantidad de artículos comprados al usuario y muestre los 
gastos de envío.
'''
def envio(cantidad):
    primer=10.95
    adicional=2.95
    return round((cantidad-1)*adicional+primer, 2)

cantidad_eltos=int(input("Ingrese la cantidad de elementos que desea pedir: \n"))
print(f"Total a pagar: ${envio(cantidad_eltos)}")