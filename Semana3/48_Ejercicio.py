"""
Desarrollare un menu,
con multiples opciones que tambien incluira la opcion de "salir" del programa
"""

while True:
    print("1 - SUMA")
    print("2 - RESTA")
    print("3 - SALIR")

    opc = int(input("Elige tu opcion y luego presiona ENTER: "))
    if opc == 1:
        print("Estas sumando!")
    elif opc == 2:
        print("Estas restando!")
    elif opc == 3:
        print("Estas saliendo!")
        break
    else:
        print("Elige una opcion valida!")