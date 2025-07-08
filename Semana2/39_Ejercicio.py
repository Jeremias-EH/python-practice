"""
Detectare si el numero ingresado es divisible por 5 y 7
"""

num1 = int(input("Ingrese el numero a comprobar: "))

if num1 % 5 == 0 and num1 % 7 == 0:
    print("Es divisible entre 5 y 7!")
else:
    print("No es divisible entre 5 y 7...")