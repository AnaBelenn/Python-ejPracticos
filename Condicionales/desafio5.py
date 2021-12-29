'''
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio y el tipo de barrio 
(CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre 
posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
'''
nombre_barrio=input("Ingrese el nombre del barrio:\n")
nombre_barrio = nombre_barrio.lower()
zona_barrio=input("Ingrese la zona del barrio: Centrico - No Centrico.\n")
zona_barrio = zona_barrio.lower()
if zona_barrio=="centrico":
    if nombre_barrio<="m":
        print(f"El barrio {nombre_barrio} se encuentra en la seccion A.")
    else:
        print(f"El barrio {nombre_barrio} se encuentra en la seccion B")
elif zona_barrio == "no centrico":
    if nombre_barrio>="m":
        print(f"El barrio {nombre_barrio} se encuentra en la seccion A.")
    else:
        print(f"El barrio {nombre_barrio} se encuentra en la seccion B")
else:
    print("Ingreso de zona invalida.")

    