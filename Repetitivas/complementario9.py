'''
Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. Desea obtener de todas las 
personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales 
y estudios de posgrado.
'''
personas=0
primaria=0
secundaria=0
tecnica=0
profesionales=0
posgrado=0
conf=input("Desea comenzar a cargar datos? S/N\n").upper()
while conf == "S":
    estudios=int(input("Estudios alcanzados: \n1- Primaria\n2- Secunadaria\n3- Carrera técnica\n4- Estudios profesionales\n5-Estudios de posgrado\n"))
    if estudios == 1:
        primaria += 1
        personas+=1
    elif estudios == 2:
        secundaria += 1
        personas+=1
    elif estudios == 3:
        tecnica += 1
        personas+=1
    elif estudios == 4:
        profesionales += 1
        personas+=1
    elif estudios == 5:
        posgrado += 1
        personas+=1
    else: 
        print("Fuera de rango")
        continue
    conf=input("Desea cargar mas datos? S/N\n").upper()
print(f"Total de personas encuestadas: {personas}\nPorcentaje de personas con estudios primarios: {primaria*100/personas}%\nPorcentaje de personas con estudios secundarios: {secundaria*100/personas}%\nPorcentaje de personas con estudios en carrera técnica: {tecnica*100/personas}%\nPorcentaje de personas con estudios profesionales: {profesionales*100/personas}%\nPorcentaje de personas con estudios de posgrado: {posgrado*100/personas}%\n")
