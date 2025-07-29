"""
Escribire una funcion para calcular el volumen de un cilindro
"""

import math

def volumen(radio, altura):
    return math.pi * radio ** 2 * altura

resultado = volumen(3,5)

print(resultado)