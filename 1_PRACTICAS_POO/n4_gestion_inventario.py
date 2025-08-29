# Sistema Gestor de Inventario

class Producto:
    def __init__(self, ID, nombre, precio):
        self.__ID = ID
        self.__nombre = nombre
        self.__precio = precio
    
    def obtener_ID(self):
        return self.__ID
    
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio
    
    def obtener_precio_con_impuesto(self):
        return self.obtener_precio() + (self.obtener_precio() * 0.10)
    
    def __str__(self):
        return f'ID: {self.__ID}\nNombre: {self.__nombre}\nPrecio: {self.__precio}'

class Electronico(Producto):
    def __init__(self, ID, nombre, precio, garantia_meses):
        super().__init__(ID, nombre, precio)
        self.__garantia_meses = garantia_meses

    def obtener_precio_con_impuesto(self):
        return self.obtener_precio() + (self.obtener_precio() * 0.15)

class Alimento(Producto):
    def __init__(self, ID, nombre, precio, fecha_vencimiento):
        super().__init__(ID, nombre, precio)
        self.__fecha_vencimiento = fecha_vencimiento

    def obtener_precio_con_impuesto(self):
        return self.obtener_precio() + (self.obtener_precio() * 0.08)

class Inventario:
    def __init__(self):
        self.__productos = []
        self.__valor_total = 0
    
    def agregar_producto(self, objeto):
        self.__productos.append(objeto)

    def obtener_valor_total_inventario(self):
        for objeto in self.__productos:
            self.__valor_total += objeto.obtener_precio_con_impuesto()
        return self.__valor_total

    def buscar_por_id(self, ID):
        for buscar_objeto in self.__productos:
            if buscar_objeto.obtener_ID() == ID:
                return buscar_objeto
                break
        return None

inventario = Inventario()
pr1 = Electronico('E001', 'Laptop', 3000, 6)
pr2 = Electronico('E002', 'Mouse', 400, 3)
pr3 = Electronico('E003', 'TV', 15000, 12)
pr4 = Electronico('E004', 'Reloj', 800, 5)
pr5 = Alimento('A001', 'Leche', 21, '20/09/25')
pr6 = Alimento('A002', 'Azucar', 40, '15/12/25')
pr7 = Alimento('A003', 'Lenteja', 20, '29/01/26')
pr8 = Alimento('A004', 'Cereal', 51, '18/02/26')

inventario.agregar_producto(pr1)
inventario.agregar_producto(pr2)
inventario.agregar_producto(pr3)
inventario.agregar_producto(pr4)
inventario.agregar_producto(pr5)
inventario.agregar_producto(pr6)
inventario.agregar_producto(pr7)
inventario.agregar_producto(pr8)

valor_total_inventario = inventario.obtener_valor_total_inventario()
print(valor_total_inventario)

buscar_id = inventario.buscar_por_id('A001')
if buscar_id:
    print(buscar_id)

print(inventario.buscar_por_id('A005'))
