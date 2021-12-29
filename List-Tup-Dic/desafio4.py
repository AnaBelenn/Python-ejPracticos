'''
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.
Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se 
encuentran a partir de la posición i.

especies = list()
conf = input("Desea ingresar una especie? S/N \n").upper()
while conf == "S":
    especies.append(input("Ingrese el nombre de la especie: \n"))
    conf = input("Desea ingresar otra especie? S/N \n").upper()
especie_tupla = tuple(especies)
for elto in especie_tupla:
    print(f"¡Hola! Soy {elto}, cuidame.")
'''
especies=list()
conf = input("Desea ingresar una especie? S/N \n").upper()
while conf == "S":
    especies.append(input("Ingrese el nombre de la especie: \n"))
    conf = input("Desea ingresar otra especie? S/N \n").upper()
especie_tupla = tuple(especies)
inicio=int(input("Posición donde desea comenzar? \n"))
cantidad= int(input("Cantidad de animales que desea buscar?\n"))
if (inicio+cantidad<=len(especie_tupla)):
    if inicio==0:
        for elto in range(0, cantidad+1):
            print(f"¡Hola! Soy {especie_tupla[elto]}, cuidame.")
    else:
        for elto in range(inicio, inicio+cantidad+1):
            print(f"¡Hola! Soy {especie_tupla[elto-1]}, cuidame.")
else:
    print("Fuera de rango.")
