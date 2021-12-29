'''
Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:
a) porcentaje de varones menores de 15 años para cada zona
b) porcentaje de varones menores de 15 años para todo el municipio
Los datos vienen ordenados por zona. Con dato de zona igual a 0, se indica el fin.
'''
continuar = True
print("Buenos días, bienvenido al sistema del Municipio \n")
print()
contador_menores_de_15 = 0
contador_menores_de_15_por_zona = 0
contador_total = 0
contador_zona = 0
zona_actual = ""
primera_vez = True
while continuar == True:
    zona = str(input("Ingrese zona de la que desea calcular porcentaje: \n"))
    edad = int(input("Ingrese edad de la persona: \n"))
    contador_total += 1
    contador_zona += 1
    if edad <= 15 :
        contador_menores_de_15 += 1
        if primera_vez:
            zona_actual = zona
            primera_vez = False
        if zona_actual != zona:
            porcentaje_total_zona = (contador_menores_de_15_por_zona / contador_zona) * 100
            print("Total Zona {0}: {1}".format(zona_actual, contador_menores_de_15_por_zona))
            print("Porcentaje total {0}: {1} %".format(zona_actual, porcentaje_total_zona))
            zona_actual = zona
            contador_menores_de_15_por_zona = 0
            contador_zona = 0
        contador_menores_de_15_por_zona += 1
    continuar_input = str(input("Desea Continuar?: (si/no) \n"))
    if( continuar_input.lower() == 'no'):
        continuar = False
print("Total Zona {0}: {1}".format(zona_actual, contador_menores_de_15_por_zona))
porcentaje_total = (contador_menores_de_15_por_zona / contador_zona) * 100
print("Porcentaje total {0}: {1} %".format(zona_actual, porcentaje_total))

porcentaje_total = (contador_menores_de_15 / contador_total) * 100
print("Porcentaje Total Municipio: {0} %".format(porcentaje_total))