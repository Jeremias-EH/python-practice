"""
Creare una clase llamada rectangulo con lo siguiente:
Base y Altura.
"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Area(self):
        return self.base * self.altura
    
    def Perimetro(self):
        return 2 * (self.base + self.altura)
    
resultado = Rectangulo(5, 3)

print(f"Area: {resultado.Area()}")
print(f"Perimetro: {resultado.Perimetro()}")