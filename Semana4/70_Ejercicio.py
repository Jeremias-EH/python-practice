"""
Funcion para calcular el porcentaje de desempleo
"""

def desempleo():
    trabajadores = int(input("Ingrese la cantida de trabajadores: "))
    desempleados = int(input("Ingrese la cantidad de desempleados: "))
    return (desempleados/trabajadores) * 100

resultado = desempleo()

print("El porcentaje de desempleados es: ", resultado, "%")