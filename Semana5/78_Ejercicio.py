"""
Creare la clase Persona, con los atributos de nombre y edad.
Un constructor para los datos, donde puedan estar vacios.
Los setters y getters para cada uno de los atributos
"""

class Persona:
    def __init__(self, Nombre=None, Edad=None):
        self._Nombre = Nombre
        self._Edad = Edad
    
    @property
    def Nombre(self):
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, nuevo_nombre):
        self._Nombre = nuevo_nombre

    @property
    def Edad(self):
        return self._Edad
    
    @Edad.setter
    def Edad(self, nueva_edad):
        self._Edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)

    def mayor_edad(self):
        if self._Edad >= 18:
            return True
        else:
            return False
    

persona1 = Persona('Jose', 52)
print(persona1.mayor_edad())
persona1.mostrar()