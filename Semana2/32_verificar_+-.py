"""
Verificare si el numero ingresado por consola es 
positivo, negativo o cero
"""

num1 = int(input("Ingrese un numero: "))

if num1 > 0:
    print("Es positivo")
elif num1 < 0:
    print("Es negativo")
elif num1 == 0:
  print("Es cero")