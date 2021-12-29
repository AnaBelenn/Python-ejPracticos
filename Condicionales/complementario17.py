'''
Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, siendo:
- estatura media de mujeres adultas: 1,65 m.
- estatura media de varones adultos: 1,72 m.
'''
sexo=input("Ingrese sexo de la persona: F/M\n").upper()
altura=int(input("Ingrese altura en cm: \n"))
if sexo== "F":
    if altura>=165:
        print("La altura ingresada es superior a la altura media de las mujeres.")
    else:
        print("La altura ingresada es inferior a la altura media de las mujeres.")
else: 
    if altura>=172:
        print("La altura ingresada es superior a la altura media de los hombres.")
    else:
        print("La altura ingresada es inferior a la altura media de los hombres.")