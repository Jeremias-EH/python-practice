"""
Simulare el lanzamiento de un dado hasta que salga 6.
"""

import random

while True:
    jugar = input("Tira el dado con 'T'!!: ")
    if jugar.lower() == 't':
        dado = random.randint(1, 6)
        if dado == 6:
            print("Salio: " , dado , ". Ganaste!")
            break
        else:
            print("Salio: " , dado , ". Vuelve a tirar!")