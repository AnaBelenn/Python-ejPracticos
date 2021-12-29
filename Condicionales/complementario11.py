'''
Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; 
desaprueba en caso contrario.
'''
nota1=float(input("Ingrese la primer calificacion: \n"))
nota2=float(input("Ingrese la segunda calificacion: \n"))
nota3=float(input("Ingrese la tercer calificacion: \n"))
total=nota1+nota2+nota3
promedio= total/3
if promedio>=70:
    print(f"Alumno aprobado con un promedio de {round(promedio, 2)}")
else: 
    print(f"Alumno reprobado con un promedio de {round(promedio, 2)}")