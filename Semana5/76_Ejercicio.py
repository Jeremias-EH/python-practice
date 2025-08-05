"""
Creare la clase Auto, con los atributos: marca, modelo, matricula y kilometraje.
"""

class Auto:
    def __init__(self, Marca, Modelo, Matricula, Kilometros):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Matricula = Matricula
        self.Kilometros = Kilometros

    def Avanzar(self, kilometros):
        self.Kilometros = self.Kilometros + kilometros

'''Defino los atributos'''
auto1 = Auto('Ford', 2018, 'RX 450 JX', 50 )
'''Se imprimen los atributos a continuacion'''
print(auto1.__dict__)
'''Ahora con esta funcion, modifique los atributos'''
auto1.Avanzar(8000)
print(auto1.__dict__) 