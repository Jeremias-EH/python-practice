"""
Elevare al cuadrado una lista de numeros utilizando amp()
"""

def elevado(x):
    return x ** 2

numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrado = list(map(elevado, numeros))

print(numeros)
print(cuadrado)