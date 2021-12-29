'''
Elaborar un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"
'''

tamanio=int(input("Ingrese el tamaño del pez:\n1- Tamaño normal\n2- Tamaño por debajo de lo normal\n3- Tamaño por encima de lo normal\n4- Tamaño sobredimensionado\nSeleccione una opcion.\n"))
if tamanio==1:
    print("Pez en buenas condiciones.")
elif tamanio==2:
    print("Pez con problemas de nutrición.")
elif tamanio==3:
    print("Pez con síntomas de organismo contaminado.")
elif tamanio==4:
    print("Pez contaminado.")
else:
    print("Error: Fuera de rango.")
