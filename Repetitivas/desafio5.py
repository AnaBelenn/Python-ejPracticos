'''
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.
Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el 
siguiente significado:
- 3 letras: Correspondientes a la patente.
- Del valor numérico:
    - Los 3 primeros números corresponden a la patente
    - El 4 número indica
        1 - Tiró basura a la vía pública
        0 - No tiró basura a la vía pública
    - El 5 número indica
        1 - Ya había sido multado el vehículo
        0 - Vehículo sin multas.
Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido 
multados.
'''
observados = 0
tirado_basura = 0
porcentaje_multados = 0
multados = 0
conf = input("Desea ingresar un vehículo? S/N\n").upper()
while conf == "S":
    vehiculo = input("Ingrese los datos: \n")
    if int(vehiculo[6])==1:
        tirado_basura += 1
    if int(vehiculo[7])==1:
        multados += 1
    observados += 1
    conf=input("Desea continuar?")
porcentaje_multados = (multados*100)/observados
print(f"Vehiculos observados: {observados}\nVehiculos que han tirado basura: {tirado_basura}\nPorcentaje ya multado: {porcentaje_multados}\n")