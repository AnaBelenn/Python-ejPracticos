'''
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 
Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o 
chicle, e imprima la cantidad de años que tarda en degradarse.
'''
def tiempo_degradar(elto: str):
    tipo= elto.lower()
    if tipo == "bolsa de plastico":
        print(f"{elto} tarda 150 años en degradarse.")
    elif tipo == "botella pet":
        print(f"{elto} tarda casi 1000 años en degradarse.")
    elif tipo == "envase tetrabrik":
        print(f"{elto} tarda hasta 30 años en degradarse.")
    elif tipo == "chicle":
        print(f"{elto} tarda 5 años en degradarse.")


elemento= input("Ingrese el tipo de elemento y averigue cuanto tarda en degradarse: \n")
tiempo_degradar(elemento)