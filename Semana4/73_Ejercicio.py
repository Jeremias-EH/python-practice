"""
Creare una Clase Circulo para calcular su area y perimetro
"""

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def Area(self):
        return math.pi * self.radio**2
    def Perimetro(self):
        return 2 * math.pi * self.radio
    
Rta = Circulo(5)

print(f"El area es: {Rta.Area()}")
print(f"El perimetro es: {Rta.Perimetro()}")