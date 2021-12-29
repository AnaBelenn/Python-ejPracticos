'''
Diseña un programa al que se proporcione como entradas dos enteros y un carácter. El programa deberá sumar, restar, multiplicar o dividir 
los valores de los dos primeros parámetros dependiendo del código indicado en el tercer parámetro, y devolver el resultado. Por ejemplo si 
el usuario ingresa la opción “S”, se deberán sumar los números.
'''
operacion=input("Ingrese dos numeros y luego la operacion que desea realizar:\nS para suma\nR para resta\nM para multiplicacion\nD para division\n") .upper()
num1=int(operacion[0])
num2=int(operacion[1])
if operacion[2]=="S":
    print(f"Suma de {num1} + {num2} = {num1+num2}")
elif operacion[2] == "R":
    print(f"Resta de {num1} - {num2} = {num1-num2}")
elif operacion[2] == "M":
    print(f"Multiplicacion de {num1} * {num2} = {num1*num2}")
elif operacion[2] == "D":
    print(f"Division de {num1} / {num2} = {num1/num2}")
else: 
    print("Opcion no valida.")