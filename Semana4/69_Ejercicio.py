"""
Funcion para calcular tiempo de viaje, con datos que de el usuario.
"""

def tiempo():
    velocidad = int(input("Ingrese la velocidad en Km/H: "))
    distancia = int(input("Ingrese la distancia en Km: "))
    return distancia/velocidad

resultado = tiempo()

print(resultado)