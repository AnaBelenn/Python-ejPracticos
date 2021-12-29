'''
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. Luego obtener 
estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, 
más de 200 colillas.
'''
colillas=0
cant=0
menos100=0
mas100=0
mas200=0
personas=0
conf=input("Desea ingresar nuevas colillas? S/N\n")
conf=conf.upper()
while conf == "S":
    cant=int(input("Ingrese el numero de colillas que recogio la persona:\n"))
    colillas= colillas + cant
    if cant<=100:
        menos100+=1
    elif cant>100 and cant<200:
        mas100+=1
    else:
        mas200+=1
    personas+=1
    conf=input("Desea ingresar nuevas colillas? S/N\n")
menos100=menos100*100/personas
mas100=mas100*100/personas
mas200=mas200*100/personas
print(f"Se recolectaron {colillas} colillas en total por {personas} personas. \nDe todas ellas, un {menos100}% recolectó menos de 100.\n El {mas100}% recolectó mas de 100 y menos de 200.\n El {mas200}% recolectó mas de 200.")

