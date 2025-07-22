"""
Solicitare que el usuario ingrese un numero y luego
imprimire la lista de multiplicar de ese numero.
"""
print("Ingrese el numero para ver su tabla de multiplicar")
numero = int(input("Ingrese el numero: "))

for i in range(1, 11):
    total = numero * i
    print({numero} ,"x" ,{i} ,"=", {total} )