'''
Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. Incluya un programa 
principal que lea tres valores del usuario y muestre su mediana.
Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. Se puede encontrar usando declaraciones 
if, o con un poco de creatividad matemática.
'''
def medio(num1, num2, num3):
    suma=num1+num2+num3
    return round(suma/3, 2)

n1=int(input("Ingrese el primer valor: \n"))
n2=int(input("Ingrese el segundo valor: \n"))
n3=int(input("Ingrese el tercer valor: \n"))
print(f"El valor medio de los numeros ingresados es {medio(n1, n2, n3)}")