'''
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
- Ingredientes comunes: Verduras y berenjena.
- Ingredientes Receta 1: Lentejas y apio.
- Ingredientes Receta 2: Morrón y Cebolla..
Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se 
debe mostrar por pantalla la receta elegida y todos los ingredientes.
'''
receta = int(input("Que tipo de receta desea? \n1- Receta 1.\n2- Reseta 2. Seleccione un numero."))
r_comun = ["Verduras", "Berenjena"]
r1 = ["Lentejas", "Apio"]
r2 = ["Morron", "Cebolla"]
ingredientes=list()
n=0
print("Seleccione solo tres ingredientes.")
while n<3:
    if receta == 1:
        print(r1 + r_comun)
        ing= input("Ingrediente: ")
        ingredientes.append(ing)
        if ing in r1:
            r1.remove(ing)
        elif ing in r_comun:
            r_comun.remove(ing)
        else:
            print("Opcion invalida")
    if receta == 2:
        print(r2 + r_comun)
        ing= input("Ingrediente: ")
        ingredientes.append(ing)
        if ing in r2:
            r2.remove(ing)
        elif ing in r_comun:
            r_comun.remove(ing)
        else:
            print("Opcion invalida")
    n+=1
print(f"Receta: {receta} - Ingredientes: {ingredientes}")