ciudades = {"Resistencia":56, "Corrientes":102, "Buenos Aires":657, "Bariloche": 99, "Formosa": 1003}

def separar(lista):
    '''
    Esta función separa en 2 diccionarios distintos a las ciudades que plantan árboles: uno con las ciudades que plantaron
    más de 100 árboles, y otro con el resto.
    '''
    mayor = []
    menor_igual = []
    for i in lista:
        if lista[i] > 100:
            mayor.append(i)
        else:
            menor_igual.append(i)
    mayor.sort()
    menor_igual.sort()
    return mayor, menor_igual

print()
print("CIUDAD         ÁRBOLES PLANTADOS")
for i in ciudades:
    print(i.ljust(20), ciudades[i])

print()
lista1, lista2 = separar(ciudades)

print(f"{len(lista1)} ciudades plantaron más de 100 árboles:")
for i in lista1:
    print(i.ljust(15), ciudades[i])
print()