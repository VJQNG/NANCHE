'''Pilas(Stacks): LIFO(last in first out)'''
class Pila:
    def __init__(self):
        self.__cosa = []

    def mostrar(self):
        print(self.__cosa)

    def agregar(self, elemento):
        self.__cosa.append(elemento)
    
    def borrar(self):
        if self.__cosa:
            self.__cosa.pop()
        else:
            print('Está vacio')

'''Colas(Queues): FIFO(First in Firt out)'''
class Cola(Pila):
    def __init__(self):
        self.__cosa = []

    def mostrar(self):
        print(self.__cosa)

    def agregar(self, elemento):
        self.__cosa.append(elemento)

    def borrar(self):
        if self.__cosa:
            self.__cosa.pop(0)
        else:
            print('Está vacio')
 
historial_web = Pila()
historial_web.agregar('google.com')
historial_web.agregar('github.com')
historial_web.agregar('grupolafragua.com')
historial_web.mostrar()
historial_web.borrar()
historial_web.mostrar()

imprimir = Cola()
imprimir.agregar('foto')
imprimir.agregar('tarea_viernes')
imprimir.agregar('Planeación')
imprimir.mostrar()
imprimir.borrar()
imprimir.mostrar()
