"""
Combinare 2 listas en pares usando la funcion "zip()"
"""

list1 = [1,2,3,4,5,6]

list2 = ["a", "x", "e", "f", "g" , "h"]

combinacion = list(zip(list1 , list2))

print("La combinacion de ambas listas quedaria asi: " , combinacion)