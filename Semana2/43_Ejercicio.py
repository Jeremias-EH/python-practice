"""
Voy a solicitar que ingresen un numero al azar,
luego se imprimira toda la suma de los numeros hasta el numero ingresado
"""

num1 = int(input("Ingrese el numero limite: "))
referencia = 1
cont = 0

while referencia <= num1:
    cont = cont + referencia
    referencia = referencia + 1

print("La suma de todos los numeros hasta el limite dado, es de: " , cont)