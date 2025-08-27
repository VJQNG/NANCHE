# Concesionario para gestionar diferentes tipos de vehiculos.

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def info(self):
        print(f'Marca: {self._marca}\nModelo: {self._modelo}\n Año: {self._anio}')

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_combustible):
        super().__init__(marca, modelo, anio)
        self.__tipo_combustible = tipo_combustible

    def claxon(self):
        print('Honk!!! Honk!!!')

    def info(self):
        print(f'Marca: {self._marca}\nModelo: {self._modelo}\nAño: {self._anio}\nCombustible: {self.__tipo_combustible}')

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.__cilindrada = cilindrada

    def caballito(self):
        print('Wiii!!!')

    def info(self):
        print(f'Marca: {self._marca}\nModelo: {self._modelo}\nAño: {self._anio}\nCilindrada: {self.__cilindrada}')

coche = Coche('Ford', 'Fiesta Ikon', '2002', 'Gasolina')
coche.info()
coche.claxon()
moto = Motocicleta('Italika', 'Mortal', '2010', '120')
moto.info()
moto.caballito()

