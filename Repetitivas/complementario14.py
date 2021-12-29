'''
Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. El precio de 
venta será 1.5 veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. En particular el costo total se 
calcula sumando:
- un costo fijo de preparación.
- un costo variable que es proporcional al tamaño de la pizza.
- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).
'''
precio_ing=float(input("Precio individual del ingrediente extra: $"))
conf=input("Desea encargar una pizza? S/N\n").upper()
while conf == "S":
    tamanio=input("Ingrese el tamaño de la pizza:\nGrande\nMediana\nPequeña\nTamaño seleccionado: ").upper()
    ingredientes=int(input("Ingrese la cantidad de ingredientes extra: \n"))
    if tamanio== "GRANDE":
        precio=float(input("Ingrese el precio de una pizza de tamaño GRANDE: \n$"))
    elif tamanio == "MEDIANA":
        precio=float(input("Ingrese el precio de una pizza de tamaño MEDIANO: \n$"))
    elif tamanio == "PEQUEÑA":
        precio=float(input("Ingrese el precio de una pizza de tamaño PEQUEÑO: \n$"))
    else:
        print("Opcion no valida.")
        break
    print(f"Precio final de la pizza: ${1.5*(precio+(ingredientes*precio_ing))}")
    conf=input("Desea encargar otra pizza? S/N\n").upper()
print("Fin del programa.")