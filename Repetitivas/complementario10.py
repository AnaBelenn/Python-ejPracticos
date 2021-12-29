'''
Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.
'''
conf=input("Desea obtener el perimetro de un triángulo? S/N\n").upper()
while conf=="S":
    lado1=float(input("Ingrese la medida del lado 1:\n"))
    lado2=float(input("Ingrese la medida del lado 2:\n"))
    lado3=float(input("Ingrese la medida del lado 3:\n"))
    print(f"Perimetro: {lado1+lado2+lado3}")
    conf=input("Desea obtener el perimetro de otro triángulo? S/N\n").upper()
print("Fin del programa.")