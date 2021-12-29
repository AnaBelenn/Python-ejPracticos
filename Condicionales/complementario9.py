'''
En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme 
a la sig. tabla:
ÁREA 		PORCENTAJE
Pediatría	    60%
Traumatología	20%
Kinesiología	20%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.
'''
presupuesto=float(input("Ingrese presupuesto anual del hospital:\n"))
print(f"El area de Pediatria recibirá un total de ${presupuesto*0.6}")
print(f"El area de Traumatología recibirá un total de ${presupuesto*0.2}")
print(f"El area de Kinesiología recibirá un total de ${presupuesto*0.2}")