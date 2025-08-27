# Imagina que quieres crear un sistema básico para gestionar libros en una biblioteca.

class Libro:
    def __init__(self, titulo, autor, prestado = False):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = prestado

    def estado(self):
        return self.__prestado

    def prestar_libro(self):
        if self.__prestado:
            print('No esta disponible')
        else:
            self.__prestado = True

    def devolver_libro(self):
        if self.__prestado:
            self.__prestado = False
        else:
            print('Esta disponible')

mi_libro = Libro('Hellboy', 'Mike Mignola')
print(mi_libro.estado())
mi_libro.prestar_libro()
print(mi_libro.estado())
mi_libro.prestar_libro()
mi_libro.devolver_libro()
print(mi_libro.estado())
