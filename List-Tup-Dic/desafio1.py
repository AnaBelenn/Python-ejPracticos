'''
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista 
y los muestre por pantalla ordenados de menor a mayor. 
'''
conf=input("Desea ingresar datos? S/N\n").upper()
lista=list()
while conf == "S":
    conocimiento=int(input("Cuanto conoce sobre contaminación en una escala del 1 al 10?\n"))
    lista.append(conocimiento)
    conf = input("Desea ingresar mas datos? S/N\n").upper()
print(sorted(lista))