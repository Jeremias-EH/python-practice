"""
Creare la clase Persona y la clase Estudiante.
La clase persona tendra el atributo nombre y el metodo mostrar_nombre()
La clase Estudiante debe heredar de la clase persona y utilizar el metodo mostrar_nombre() de la clase Persona
"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_nombre(self):
        print(self.nombre)

class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def mostrar(self):
        super().mostrar_nombre()

estudiante1 = Estudiante('Lucas')
estudiante1.mostrar()