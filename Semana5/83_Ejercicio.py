"""
Convertire un string de numeros a numeros enteros utilizando map()
"""

def Convertir_a_Entero(cadena):
    return int(cadena)

string = ['1', '2', '3', '4', '5']

entero = list(map(Convertir_a_Entero, string))

print(string)
print(entero)