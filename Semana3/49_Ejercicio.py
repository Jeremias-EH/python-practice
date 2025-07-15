"""
Desarrollare el juego de la moneda
"""

import random

while True:
    jugar = input("Tirar la moneda?(s/n): ")
    if jugar.lower() == "s":
        moneda = random.randint(1, 2)
        if moneda == 1:
           print("SALIO: CARA")
        else:
           print("SALIO: CRUZ")
    if jugar.lower() == "n":
       break
    if jugar.lower() != "n" and jugar.lower() != "s":
          print("Elige 's' o 'n'!!!")
print("Gracias por jugar!")