'''
El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. De cada consulta tiene como datos: la edad del menor y el 
día de visita. Los datos están ordenados en forma creciente por día. Proponer un fin de datos para cada día. Se desea conocer, para cada 
día, la edad promedio de pacientes y además el día en que se registró el máximo de pacientes.
'''

print("Centro de Salud de Rosario.")
continuar=input("Desea comenzar? S/N\n").upper()
dia=""
acum_edad=0
edad_promedio=0
pacientes=0
maximo_pacientes=""
primer_ingreso=True
pacientes_anteriores=0
while continuar=="S":
    dia_visita=input("Ingrese la fecha del registro:\n")
    edad_paciente=int(input("Ingrese la edad del paciente:\n"))
    if primer_ingreso:
        dia=dia_visita
        primer_ingreso=False
    if dia == dia_visita:
        acum_edad+= edad_paciente
        pacientes+=1
    else:
        edad_promedio=acum_edad/pacientes
        if pacientes_anteriores==0:
            pacientes_anteriores=pacientes
            maximo_pacientes=dia
        elif pacientes_anteriores<pacientes:
            maximo_pacientes=dia
        print(f"Dia: {dia}\nCantidad de pacientes: {pacientes}\nEdad promedio de pacientes: {round(edad_promedio, 2)}")
        dia=dia_visita
        pacientes=0
        acum_edad=0
        continuar
        continuar=input("Desea ingresar otra fecha? S/N\n").upper()
if primer_ingreso==True:
    print("No se ingresaron datos. Fin del programa.")
else:
    print(f"Dia con mayor cantidad de pacientes: {maximo_pacientes}")