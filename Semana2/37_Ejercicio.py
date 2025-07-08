"""
Determinar si un caracter es vocal
"""

caracter = input("Ingrese el caracter(Letra): ")
vocales = ["a", "e", "i", "o", "u"]
if caracter.lower() in vocales:
    print("El caracter ingresado, es VOLCA.")
else:
    print("El caracter ingresado NO ES VOCAL")