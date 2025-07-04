"""
Eliminare duplicados de una lista
"""

lista1 = [1,2,2,3,3,3,4,5,5,5,5,6]

lista_limpia = list(set(lista1))

print("La lista se ve asi: " , lista1 , "y asi se ve una ves eliminado los numeros duplicados: " , lista_limpia)