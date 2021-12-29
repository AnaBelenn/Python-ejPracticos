'''
Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y devuelva la 
hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que lea 
las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa 
y muestre el resultado.
'''
import math

def func_hipot(lado1, lado2):
    cuadrados= math.sqrt(lado1**2 + lado2**2)
    return round(cuadrados, 2)

lado1=int(input("Ingrese el lado 1:\n"))
lado2=int(input("Ingrese el lado 2:\n"))
print(f"Hipotenusa: {func_hipot(lado1, lado2)}")