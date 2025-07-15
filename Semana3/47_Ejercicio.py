"""
solicitar ingreso de numero y luego se imprime la cantidad de digitos.
"""

num1 = int(input("Ingrese un numero: "))
cont = 0
while num1 != 0:
    num1 = num1 // 10 
    cont = cont + 1

print("El numero de digitos es: ", cont)