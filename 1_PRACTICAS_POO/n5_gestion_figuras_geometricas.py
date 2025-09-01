# El objetivo es crear un sistema para calcular el área y el perímetro de diferentes figuras geométricas, asegurando que los cálculos se manejen de manera segura y flexible.

class FiguraGeometrica:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def obtener_nombre(self):
        return self.__nombre

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.__radio = radio

    def calcular_area(self):
        return f'Area: {round(3.141592654 * (self.__radio ** 2), 2)}' # pi*radio**2

    def calcular_perimetro(self):
        return f'Perimetro: {round(2 * 3.141592654 * self.__radio, 2)}' # 2*pi*radio

class Cuadrado(FiguraGeometrica):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.__lado = lado

    def calcular_area(self):
        return f'Area: {round(self.__lado ** 2, 2)}'

    def calcular_perimetro(self):
        return f'Perimetro: {round(self.__lado * 4, 2)}'

class LoteFiguras:
    def __init__(self):
        self.__coleccion_figuras = []

    def agregar_figura(self, figura):
        self.__coleccion_figuras.append(figura)

    def imprimir_informe(self):
        for figura in self.__coleccion_figuras:
            print(f'{figura.obtener_nombre()}\n{figura.calcular_area()}\n{figura.calcular_perimetro()}')

figuras = LoteFiguras()

circulo = Circulo('Circulo', 5)
cuadrado = Cuadrado('Cuadrado', 5)

figuras.agregar_figura(circulo)
figuras.agregar_figura(cuadrado)

figuras.imprimir_informe()
