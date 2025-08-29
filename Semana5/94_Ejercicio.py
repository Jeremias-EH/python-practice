"""
Voy a filtrar los numeros negativos de una lista utilizando filter
"""

lista1 = [10,-20,30,-40]

negativos = list(filter(lambda x:x<0, lista1))

print(lista1)
print(negativos)