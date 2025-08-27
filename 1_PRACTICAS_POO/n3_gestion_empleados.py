# Sistema gestion de empleados

class Empleado:
    def __init__(self, nombre, ID, salario):
        self.__nombre = nombre
        self.__ID = ID
        self.__salario_base = salario
    
    def salario_base(self):
        return self.__salario_base

    def salario_neto(self):
        return self.salario_base() - (self.salario_base() * 0.10)

    def ver_nombre(self):
        return self.__nombre
    
    def __str__(self):
        return f'\nEmpleado: {self.__nombre}\nID: {self.__ID}\n'

class Desarrollador(Empleado):
    def __init__(self, nombre, ID, salario, lenguaje):
        super().__init__(nombre, ID, salario)
        self.__lenguaje_principal = lenguaje

    def salario_neto(self):
        return self.salario_base() + (self.salario_base() * 0.15)

class Gerente(Empleado):
    def __init__(self, nombre, ID, salario, departamento_gestionado):
        super().__init__(nombre, ID, salario)
        self.__departamento_gestionado = departamento_gestionado

    def salario_neto(self):
        return self.salario_base() + (self.salario_base() * 0.25)


nomina_empresa = []

dev = Desarrollador('Marcos', 'D01', 40_000, 'Python')
man = Gerente('Damaris', 'G01', 50_000, 'Direccion')

nomina_empresa.append(dev)
nomina_empresa.append(man)

for instancia in nomina_empresa:
    print(instancia)
    print(instancia.salario_base())
    print(instancia.salario_neto())
