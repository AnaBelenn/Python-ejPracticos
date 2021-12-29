'''
Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama que lea por cada estudiante la calificación obtenida y 
calcule e imprima:
A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.
B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.
C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
'''
import random
menor50=0
mayor50=0
mayor70=0
mayor80=0
for n in range(100):
    calificacion=random.randrange(0, 100)
    if calificacion<50:
        menor50+=1
    elif calificacion>=50 and calificacion<80:
        mayor50+=1    
    elif calificacion>=70 and calificacion<80:
        mayor70+=1
    else:
        mayor80+=1
print("Se evaluaron 100 alumnos:")
print(f"Estudiantes que obtuvieron una calificación menor a 50: {menor50} alumnos.")
print(f"Estudiantes que obtuvieron una calificación de 50 o más pero menor que 80: {mayor50} alumnos.")
print(f"Estudiantes que obtuvieron una calificación de 70 o más pero menor que 80: {mayor70} alumnos.")
print(f"Estudiantes que obtuvieron una calificación de 80 o más: {mayor80} alumnos.")