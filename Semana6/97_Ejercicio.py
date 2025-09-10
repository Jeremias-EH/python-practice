"""
Creare una excepcion que me ayudara a identificar
si una lista esta fuera de rango
"""

lista1 = [1,2,3,4,5,6,7,8,9,10]

try:
    print(lista1[21])
except IndexError:
    print("Error, el indice no existe.")
