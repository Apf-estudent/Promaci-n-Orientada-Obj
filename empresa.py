#Evaluación 25/09/2024
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario=salario

    def salariobase(self):
        return self.salario

    def detalles (self):
        print("Nombre: ",self.nombre, "\nSalario base: ",self.salario)

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono=bono

    def salariobase(self):
        return self.salario+self.bono

    def detalles(self):
        super().detalles()
        print("Bono anual: ",self.bono)

    def accesoinfo(self):
        print("Acceso a información")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, bono2):
        super().__init__(nombre, salario)
        self.bono2 = bono2

    def salariobase(self):
        return self.salario+self.bono2

    def detalles(self):
        super().detalles()
        print(f"Bono por proyecto: ",self.bono2)

    def accesoherramientas(self):
        print("Acceso a herramientas")

class Diseñador(Empleado):
    def __init__(self, nombre, salario, bono3):
        super().__init__(nombre, salario)
        self.bono3=bono3

    def salariobase(self):
        return self.salario+self.bono3

    def detalles(self):
        super().detalles()
        print("Bono por diseño: ",self.bono3)

    def accesosoftware(self):
        print("Acceso a software")

empleados=[
    Gerente("Ramiro", 145000, 98600),
    Desarrollador("Luka", 85000, 75000),
    Diseñador("Gertrudis", 99000, 950000)
]

for empleado in empleados:
    print(empleado.detalles())
    print("Salario total:" ,empleado.salariobase())
    print("______________________________________________")
    print()