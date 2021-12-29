'''
Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: 
Número de pulsaciones = (220 - edad)/10
'''
edad=int(input("Ingrese la edad de la persona:\n"))
print(f"Pulsaciones: {(220 - edad)//10} por cada 10seg.")