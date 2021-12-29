'''
Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
'''
cantidad=int(input("Longitud de la palabra:\n"))
palabra=list()
for n in range(cantidad):
    palabra.append(input("Ingrese la letra:\n"))

palabra2=palabra.copy()
palabra2.reverse()
palabra="".join(palabra).upper()
palabra2="".join(palabra2).upper()
if palabra == palabra2:
    print(f"{palabra} es palindromo.")
else:
    print(f"{palabra} no es palindromo.")
