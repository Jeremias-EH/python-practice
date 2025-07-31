"""
Creare la clase Libro con los siguientes atributos:
Titulo, Autor, Editorial, Añor de publicacion.
Sera con el metodo para incializar atributos
"""

class Libro:
    def __init__(self,
                 Titulo,
                 Autor,
                 Editorial,
                 Año_publicacion):
        
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.Año_publicacion = Año_publicacion

Mi_libro = Libro('Pragmatismo',
                 'Lupus Argentum',
                 'Unknow',
                 '2025')

print(Mi_libro.__dict__)