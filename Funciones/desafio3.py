'''
MODIFICAR USANDO DICCIONARIOS, TENIENDO EN CUENTA LAS MISMAS REGLAS PERO MOSTRANDO SOLO LOS NOMBRES DE LAS CIUDADES.
-------------------------------------------------------------------------------
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina 
durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda 
con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
'''
def separar(arboles):
    superan=list()
    ciudades=0
    no_superan= list()
    for elto in arboles:
        if elto > 100:
            superan.append(elto)
            ciudades += 1
        else: 
            no_superan.append(elto)
    print(f"Superan los 100 arboles plantados: {sorted(superan)}")
    print(f"No superan los 100 arboles plantados: {sorted(no_superan)}")
    print(f"Cantidad de ciudades que plantaron mas de 100 arboles durante la cuarentena: {ciudades}")

plantacion = list()
conf = input("Desea agregar elementos a la lista? S/N\n").upper()
while conf == "S":
    arboles= int(input(f"Cuantos arboles se plantaron en la ciudad?\n"))
    plantacion.append(arboles)
    conf = input("Desea agregar mas elementos? S/N\n").upper()

separar(plantacion)
