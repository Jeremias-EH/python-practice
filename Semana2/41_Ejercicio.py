"""
Calculare el IMC y lo plasmare
"""

peso = int(input("Ingrese el peso(En KG): ") )
altura = int(input("Ahora Ingrese la altura(En cm): "))
altura = altura / 100 
"""Corregi y converti los Centimetros a Metros"""
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print("Tu clasificacion es: ", IMC ,"- Peso Bajo")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Tu clasificacion es: ", IMC ,"- Peso Normal")
elif IMC >= 25 and IMC <=29.9:
    print("Tu clasificacion es: ", IMC,"- Sobrepeso")
elif IMC >= 30 and IMC <= 34.9:
    print("Tu clasificacion es: ", IMC, "- Obesidad Grado 1")
elif IMC >= 35 and IMC <= 39.9:
    print("Tu clasificacion es: ", IMC, "- Obesidad Grado 2")
elif IMC >= 40:
    print("Tu clasificacion es: ", IMC, "- Obesidad Grado 3")