"""
Voy a escribir un codigo para imprimir la cantidad de memoria ram del sistema
"""

import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()

    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

memoria = obtener_ram()

print('Ram total: ',memoria, 'Gb')