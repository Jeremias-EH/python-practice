"""
Filtrare una cadena que contenga un caracter especifico utilizando Filter
"""
string = ['Manzana','Python','Estelar']

caracter = 'a'

con_a = list(filter(lambda x:caracter in x, string))

print(string)
print(con_a)