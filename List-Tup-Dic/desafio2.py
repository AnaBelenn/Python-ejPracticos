'''
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua 
crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino 
muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero.
'''
factores_cont='Plastico', 'Petroleo', 'Residuos tóxicos', 'Pilas'
num = int(input(f"Ingrese un numero del 1 al {len(factores_cont)} para jugar o ingrese 0 para salir.\n"))
while num != 0:
    if num > len(factores_cont):
        print("Fuera de rango.")
    else:
        print("Factor contaminante: ", factores_cont[num-1])
    num = int(input(f"Ingrese un numero del 1 al {len(factores_cont)} para volver a jugar o ingrese 0 para salir.\n"))
print("Fin del juego.")
print(type(factores_cont))

