'''
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de 
al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización 
de fertilizantes.
'''

hect_comp=int(input("Ingrese porcentaje de compuesto por hectarea:\n"))
vegetacion=input("Ingrese el tipo de vegetacion:\n")
a = vegetacion.upper()
if a == 'MATORRAL':
    print("NO es factible la utilizacion de fertilizantes.")
elif a != 'MATORRAL':
    if hect_comp>=10:
        print("Es factible la utilizacion de fertilizantes.")