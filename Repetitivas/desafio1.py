'''
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le 
permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 
'''
intentos=3
print(f"Recuerde que solo tiene {intentos} intentos")
contraseña= input("Ingrese su contraseña:\n")
cont="holaMundo1"
n=1
if contraseña != cont: 
    band=False
    while n < intentos and band == False:
        print("Contraseña incorrecta.")
        contraseña = input("Ingrese la contraseña nuevamente: \n")
        if contraseña == cont:
            band = True
        else:
            intentos-=1
else: 
    band=True
if band==False:
    print("Contraseña incorrecta. Ya no tiene mas intentos.")
else:
    print("Contraseña correcta.")