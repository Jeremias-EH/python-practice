"""
Imprimir la tabla de multiplicar del numero ingresado
"""

num1 = int(input("Ingrese el numero a verificar: "))

n = 1

while n <= 10:
    print(num1, "x", n ,"=" ,{num1 * n})
    n = n + 1