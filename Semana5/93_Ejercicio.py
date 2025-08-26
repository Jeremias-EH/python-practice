"""
Filtrar cadena/string de longitud mayor a 3 de una list, usando filter
"""

string = ['Arbol', 'Nuez', 'Python', 'Pez', 'Sol']

Longitud = list(filter(lambda x:len(x) > 3, string))

print(Longitud)