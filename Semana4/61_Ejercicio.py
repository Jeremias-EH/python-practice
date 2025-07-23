"""
Imprimir la suma de los numeros pares del 1 al 10
"""
t = 0
for i in range(1, 11):
    if i % 2 == 0:
        t = t + i

print(t)