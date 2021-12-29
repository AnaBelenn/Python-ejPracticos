'''
Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
i. Si trabaja 40 horas o menos se le paga $16 por hora
ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
'''
horas_trabajadas=int(input("Ingrese las horas trabajadas: \n"))
if horas_trabajadas<=40:
    print(f"Salario semanal: ${horas_trabajadas*16}")
else:
    print(f"Salario semanal: ${(40*16)+(horas_trabajadas-40)*20}")