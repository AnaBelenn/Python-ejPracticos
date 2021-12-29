'''
Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a 
los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:
Si A>=B + C à No se trata de un triángulo
Si A2 = B2 + C2 à Es un triángulo rectángulo
Si A2 > B2 + C2 à Es un triángulo obtusángulo
Si A2 < B2 + C2 à Es un triángulo acutángulo
'''
l1=float(input("Ingrese la longitud del lado A:\n"))
l2=float(input("Ingrese la longitud del lado B:\n"))
l3=float(input("Ingrese la longitud del lado C:\n"))
if l1>=(l2+l3):
    print("No se trata de un triangulo.")
elif l1**2 == (l2**2 + l3**2):
    print("Es un triàngulo rectángulo.")
elif l1**2> (l2**2 + l3**2):
    print("Es un triángulo obtusángulo.")
elif l1**2< (l2**2 + l3**2):
    print("Es un triángulo acutángulo.")