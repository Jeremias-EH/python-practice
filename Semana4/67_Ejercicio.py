"""
Escribire una funcion para calcular el promedio de una lista de numeros
"""

def promedio(lista):
    return sum(lista) / len(lista)

resultado = promedio([1,2,3,4,5,6,7,8,9,10])

print(resultado)