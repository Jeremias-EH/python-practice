"""
Se ingresara un numero X y se imprimira el factorial de dicho numero
"""

num1 = int(input("Ingrese el numero del cual quiere saber su factorial: "))
contador = 1
var1 = 1

while contador <= num1:
    var1 = var1 * contador
    contador = contador + 1

print("El factorial del numero especificado es: " , var1)