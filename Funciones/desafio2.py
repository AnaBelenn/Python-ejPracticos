'''
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
- Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
- Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
- Si ambos números son iguales, debe devolver el nombre de ambas.
'''
def relacion(a, b):
    if a<b:
        print("La ciudad que mas toneladas recicló fue la ciudad 2.")
    elif a>b:
        print("La ciudad que mas toneladas recicló fue la ciudad 1.")
    else:
        print("Ambas ciudades reciclaron la misma cantidad de residuos.")

c1= int(input("Cuantas toneladas recicló la ciudad 1?\n"))
c2= int(input("Cuantas toneladas recicló la ciudad 2?\n"))
relacion(c1, c2)
