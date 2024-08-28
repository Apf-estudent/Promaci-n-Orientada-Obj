#Crear una clase fábrica que tenga los atributos "llantas", "color" y "precio".
#Luego crear dos clases más que hereden de fabrica, las cuales son moto y carro
#Crear metodos que muestren la cantidad de llantas,color y precio.

# Clase Fabrica, tiene atributos llantas, color y precio
class Fabrica: 
    def __init__(self, llantas, color, precio):
        # Inicializa los atributos llantas, color y precio
        self.llantas=llantas
        self.color=color
        self.precio=precio

    def detalles(self):
        # Muestra los detalles del vehiculo (llantas, color y precio)
        print("Llantas: ",self.llantas,"\nColor: ",self.color,"\nPrecio: $",self.precio)
        print("______________________________")

# Clase Moto, hereda de Fabrica y agrega atributo vehiculo
class Moto(Fabrica):
    def __init__(self, llantas, color, precio, vehiculo):
        # Inicializa los atributos llantas, color y precio de la clase Fabrica
        super().__init__(llantas, color, precio)
        # Inicializa el atributo vehiculo
        self.vehiculo=vehiculo

    def detalles(self):
        # Muestra el tipo de vehiculo
        print("Vehiculo: ",self.vehiculo)
        # Llama al metodo detalles de la clase Fabrica para mostrar los detalles del vehiculo
        super().detalles()

# Clase Carro, hereda de Fabrica y agrega atributo vehiculo2
class Carro(Fabrica):
    def __init__(self, llantas, color, precio, vehiculo2):
        # Inicializa los atributos llantas, color y precio de la clase Fabrica
        super().__init__(llantas, color, precio)
        # Inicializa el atributo vehiculo2
        self.vehiculo2=vehiculo2

    def detalles(self):
        # Muestra el tipo de vehiculo
        print("Vehiculo: ",self.vehiculo2)
        # Llama al metodo detalles de la clase Fabrica para mostrar los detalles del vehiculo
        super().detalles()

# Crea un objeto Moto con atributos llantas=2, color="Rojo", precio=1000000 y vehiculo="Motocicleta"
C1=Moto(2,"Rojo",1000000,"Motocicleta")
# Muestra los detalles del objeto Moto
C1.detalles()

C2=Carro(4,"Blanco",67888678,"Automovil")
C2.detalles()
