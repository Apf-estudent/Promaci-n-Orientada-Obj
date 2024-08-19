#Crear una clase fábrica que tenga los atributos "llantas", "color" y "precio".
#Luego crear dos clases más que hereden de fabrica, las cuales son moto y carro
#Crear metodos que muestren la cantidad de llantas,color y precio.

class Fabrica: 
    def __init__(self, llantas, color, precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio

    def detalles(self):
        print("Llantas: ",self.llantas,"\nColor: ",self.color,"\nPrecio: $",self.precio)
        print("______________________________")

class Moto(Fabrica):
    def __init__(self, llantas, color, precio,vehiculo):
        super().__init__(llantas, color, precio)
        self.vehiculo=vehiculo

    def detalles(self):
        print("Vehiculo: ",self.vehiculo)
        super().detalles()

class Carro(Fabrica):
    def __init__(self, llantas, color, precio,vehiculo2):
        super().__init__(llantas, color, precio)
        self.vehiculo2=vehiculo2

    def detalles(self):
        print("Vehiculo: ",self.vehiculo2)

        super().detalles()

C1=Moto(2,"Rojo",1000000,"Motocicleta")
C1.detalles()

C2=Carro(4,"Blanco",67888678,"Automovil")
C2.detalles()