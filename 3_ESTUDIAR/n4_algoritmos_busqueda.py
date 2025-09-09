# Busqueda lineal
'''
El objetivo es encontrar un elemento especifico dentro de una lista revisando cada elemento, uno por uno, en secuencia hasta encontrarlo se llegue hasta el final de la lista.

Ideal para listas pequeñas o si no se sabe si la lista esta ordenada

enumerate(): aplicando esta funcion a una lista: enumerate(LISTA), devuelve una tupla que contiene en indice y el elemento: (INDICE, ELEMENTO)
'''

class algoritmo:
    def __init__(self, lista):
        self.__lista = lista

    def ordenar(self):
        for todo in self.__lista.items():
            print(todo)

#dic = algoritmo(['mango', 'manzana', 'platano', 'fresa', 'piña'])
dic = algoritmo({1:'mango', 2:'manzana', 3:'platano', 4:'fresa', 5:'piña'})
dic.ordenar()
