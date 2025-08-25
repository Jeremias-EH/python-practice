"""
Duplicar cada elemento de una lista utilizando map y lambda
"""

numero = [1,2,3,4,5]
print(numero)
duplicados = list(map(lambda x:x*2, numero))
print(duplicados)