'''
elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene 
usando insecticida en su plantación. Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite revisión de suelos en su 
plantación". Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y 
cuidaremos el suelo de tu plantación".
'''
cant_anios= int(input("Ingrese la cantidad de años que usa insecticida en su plantacion: \n"))
if cant_anios<10:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación.")
else:
    print("Por favor solicite revisión de suelos en su plantación.")