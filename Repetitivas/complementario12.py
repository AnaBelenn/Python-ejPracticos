'''
Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. Debe diseñar un programa que permita monto por 
cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:
• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
• El programa finaliza cuando se introduce una D como tipo de gasolina.
'''
tipo=input("Seleccione un tipo de gasolina:\nA- Tipo A\nB- Tipo B\nC- Tipo C\nPresione D para salir\n").upper()
total=0
while tipo != "D":
    cantidad=float(input("Ingrese la cantidad de litros que compró:\n"))
    if tipo == "A":
        monto=cantidad*50
        print(f"Precio del litro: $50\nMonto a pagar: ${monto}")
    elif tipo == "B":
        monto=cantidad*55
        print(f"Precio del litro: $55\nMonto a pagar: ${monto}")
    elif tipo == "C":
        monto=cantidad*60
        print(f"Precio del litro: $60\nMonto a pagar: ${monto}")
    elif tipo =="D":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida.")
        continue
    total=total+monto
    tipo=input("Seleccione un tipo de gasolina:\nA- Tipo A\nB- Tipo B\nC- Tipo C\nPresione D para salir\n").upper()
print(f"Total recaudado en el dia: ${total}")

