"""
Filtrare elementos que sean listas
"""

lista1 = [1,2,[3,4],[5,6], ['Python', 'Hola Mundo'],10]

listas = list(filter(lambda x: isinstance(x, list), lista1))

print(lista1)
print(listas)