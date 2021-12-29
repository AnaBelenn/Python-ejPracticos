'''
Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. 
Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento
0 – 6000				15%
6000 – 7900				10%
7900 – 12000			6%
Más de 12000			 0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el 
sueldo aumentado.
'''
sueldo=int(input("Ingrese sueldo actual: \n"))
if sueldo<= 6000:
    print(f"Recibirá un aumento del 15% que equivale a {sueldo*0.15}.\n- Sueldo actual: {sueldo}\n- Sueldo aumentado: {sueldo+sueldo*0.15}")
elif sueldo <= 7900:
    print(f"Recibirá un aumento del 10% que equivale a {sueldo*0.1}.\n- Sueldo actual: {sueldo}\n- Sueldo aumentado: {sueldo+sueldo*0.1}")
elif sueldo <= 12000:
    print(f"Recibirá un aumento del 6% que equivale a {sueldo*0.06}.\n- Sueldo actual: {sueldo}\n- Sueldo aumentado: {sueldo+sueldo*0.06}")
elif sueldo > 12000:
    print(f"No recibirá aumento.\n- Sueldo: {sueldo}")