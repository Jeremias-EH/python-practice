"""
Creare una clase: Animal, que poseera los atributos: especie y nombre
"""

class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
    def hablar(self):
        if self.especie == 'Perro':
            print('Guau, guau')
        elif self.especie == 'Gato':
            print('Miau, miau')
        else:
            print('...')

perro = Animal('Perro', 'Mia')
gato = Animal('Gato', 'Luc')

perro.hablar()
gato.hablar()

print(perro.__dict__)
print(gato.__dict__)