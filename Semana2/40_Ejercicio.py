"""
Verificare si el string ingresado es "python"
"""
string = input("Ingrese su palabra: ")

comprobante = ["python"]

if string.lower() in comprobante:
    print("Si escribiste PYTHON! GENIAL!")
else:
    print("Me mentiste </3, no escribiste PYTHON...")