"""
Funcion para clasificar una sustancia en: acida, neutra o basica. Usando su Ph como indicador.
"""

def medidor():
    Ph = int(input("Ingrese el Ph de la sustancia: "))
    if Ph < 7:
        return "Ácida"
    elif Ph > 7:
        return "Básica"
    else: 
        return "Neutra"
    
resultado = medidor()

print("La sustancia es:" , resultado)