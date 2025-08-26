"""
Filtrar numeros pares de una lista utilizando filter
"""

lista1 = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda z:z % 2 == 0, lista1))
print(lista1)
print(pares)