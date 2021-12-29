'''
Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje 
que cada quien invierte con respecto a la cantidad total invertida.
'''
cantidad1=float(input("Ingrese el monto que invirtió la primer persona: "))
cantidad2=float(input("Ingrese el monto que invirtió la segunda persona: "))
cantidad3=float(input("Ingrese el monto que invirtió la tercer persona: "))
total=cantidad1+cantidad2+cantidad3
print(f"La primer persona invirtió un {round((cantidad1*100)/total, 2)}%")
print(f"La segunda persona invirtió un {round((cantidad2*100)/total, 2)}%")
print(f"La tercer persona invirtió un {round((cantidad3*100)/total, 2)}%")