"""
Creare la clase persona con los atributos:
Nombre, Edad, DNI.
Usando Init()
"""

class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mayor_de_edad(self):
        if self.edad >= 18:
            return True

resultado = Persona('Bellona', 35 , 35895675)

print(f"El nombre es: {resultado.nombre}")
print(f"La edad es: {resultado.edad} años")
print(f"El DNI es: {resultado.dni}")