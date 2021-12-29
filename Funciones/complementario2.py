'''
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos.
Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único 
resultado. Escriba un programa principal que use la función.
Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá actualizar fácilmente 
cuando las tasas aumentan.
'''
def tarifa(km):
    tarifa_base=40
    adicional=15
    tarifa_total=((km*1000)/140)*adicional+tarifa_base
    return round(tarifa_total, 2)

distancia=float(input("Ingrese la distancia recorrida en Km:\n"))
print(f"Total a pagar: ${tarifa(distancia)}")