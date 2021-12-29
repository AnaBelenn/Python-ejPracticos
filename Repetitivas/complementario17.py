'''
Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un porcentaje de su salario 
mensual que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:
Tiempo									Utilidad
Menos de 1 año					        5% del salario
Más de 1 año y hasta 2 años		        7% del salario
Más de 2 años y hasta 5 años            10% del salario
Más de 10 años						    20% del salario
'''
conf=input("Desea realizar una consulta? S/N\n").upper()
while conf=="S":
    salario=float(input("Ingrese salario mensual: \n$"))
    antiguedad=int(input("Ingrese los años de antiguedad:\n"))
    if antiguedad<1:
        utilidad=salario*0.05
    elif antiguedad<2:
        utilidad=salario*0.07
    elif antiguedad<5:
        utilidad=salario*0.1
    elif antiguedad<10:
        utilidad=salario*0.15
    else:
        utilidad=salario*0.2
    print(f"La utilidad que recibe el empleado con una antiguedad de {antiguedad} año/s es de ${round(utilidad, 2)} con un sueldo final de ${round((utilidad+salario), 2)}")
    conf=input("Desea realizar otra consulta? S/N\n").upper()
print("Fin del programa.")
