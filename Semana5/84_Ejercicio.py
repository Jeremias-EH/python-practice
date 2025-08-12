"""
Calculare la longitud de una lista utilziando map()
"""

def Longitud(palabra):
    return len(palabra)

string = ["Hola", "Buen", "Dia"]

longitudes = list(map(Longitud, string))

print(string)
print(longitudes)