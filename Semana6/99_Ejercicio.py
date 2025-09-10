"""
Escribire dentro de un archivo de texto plano, un 'hola mundo'
"""

def write(name_file, content):
    with open(name_file, "w") as file:
        file.write(content)

write('Index.html', "Hola Mundo!!!")