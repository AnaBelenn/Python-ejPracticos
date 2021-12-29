'''
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo 
contactos hasta que el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
'''
usuarios=dict()
conf = input("Desea ingresar un nuevo contacto? S/N\n").upper()
while conf=="S":
    nombre=input("Ingrese el nombre del biologo:\n")
    if nombre in usuarios:
        print("Usuario ya existente.")
    else: 
        usuarios[nombre]=input("Ingrese el correo electronico:\n")
    conf = input("Desea ingresar un nuevo contacto? S/N\n").upper()
print(usuarios)
