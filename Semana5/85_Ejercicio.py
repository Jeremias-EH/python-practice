"""
Obtener el cuadrado de la suma de dos listas, utilizando map()
"""

def suma(a,b):
    return (a+b) ** 2

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

resultado = list(map(suma, lista1, lista2))

print(lista1)
print(lista2)

print(resultado)