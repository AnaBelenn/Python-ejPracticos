'''
Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
'''
m=int(input("Ingrese el numero dividendo:\n"))
n=int(input("Ingrese el numero divisor:\n"))
if m%n==0:
    print(f"{n} es divisor de {m}")
else:
    print(f"{n} NO es divisor de {m}")