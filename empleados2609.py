
#26/09/2024
class Empleados:
    def __init__(self, nombre, id, salario, salariohora):
        self.nombre = nombre
        self.id = id
        self.salario = salario
        self.salariohora = salariohora

    def detalles(self):
        print("Nombre: ", self.nombre, "\nID: ", self.id, "\nSalario: ", self.salario, "\nHoras: ", self.salariohora)

    def salariobase(self):
        return self.salario

    def salariototal(self):
        return self.salariohora*self.salario

empleados={
    Empleados("Manuel", 7897, 10000, 6),
    Empleados("Naomi", 3923, 5000, 9),
    Empleados("Ingrid", 4621, 13000, 4)
}

for empleado in empleados:
    empleado.detalles()
    print("Salario total: ", empleado.salariototal())
    print("______________________________")
