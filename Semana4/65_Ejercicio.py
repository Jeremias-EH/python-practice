"""
Usare una funcion para verificar
si un numero es par o impar
"""

def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = par(4)
print(resultado)