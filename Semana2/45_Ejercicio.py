"""
Generare un numero aleatorio entre 1 y 10.
Luego se pedira al usuario que ingrese numeros hasta que acierte.
"""

import random

num_random = random.randint(1, 10)
intentos = 0

while True:
    num1 = int(input("Adivina el numero...: "))
    intentos = intentos + 1
    if num1 == num_random:
        print(f"Eres genial, adivinaste! Esto te tomo: " , intentos , " Intentos hasta que acertaste!")
        break