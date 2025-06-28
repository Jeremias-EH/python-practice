"""
Voy a verificar si una palabra es un palindromo (Palabras que se leen igual de izquierda a derecha que de derecha a izquierda)
"""

palabra1 = "python"
palabra2 = "radar"

verificacion1 = palabra1 == palabra1[::-1]
verificacion2 = palabra2 == palabra2[::-1]

print("La primer palabra es: " , verificacion1 )
print("La segunda palabra es: " , verificacion2)