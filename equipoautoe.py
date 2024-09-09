class EquipoDeportivo:
    def __init__(self, nombre, fecha_creacion, precio, descripcion, precio_costo, precio_venta, cantidad_stock):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.precio = precio
        self.descripcion = descripcion
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.cantidad_stock = cantidad_stock

    def vender(self, cantidadvendida):
        if cantidadvendida > self.cantidad_stock:
            print(f"No hay suficiente stock para vender {cantidadvendida} {self.nombre}.")
        else:
            self.cantidad_stock -= cantidadvendida
            print(f"Se vendieron {cantidadvendida} {self.nombre}. Cantidad en stock actual: {self.cantidad_stock}")

    def __str__(self):
        #f es de funcion, pero mas abreviado
        return f"Nombre: {self.nombre}\nFecha de creación: {self.fecha_creacion}\nPrecio: ${self.precio}\nDescripción: {self.descripcion}\nPrecio costo: ${self.precio_costo}\nPrecio venta: ${self.precio_venta}\nCantidad en stock: {self.cantidad_stock}"


class ControlStock:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def imprimir_equipos(self):
        for equipo in self.equipos:
            print(equipo)
            print("------------------------")

    def vender_equipo(self, nombre_equipo, cantidadvendida):
        for equipo in self.equipos:
            if equipo.nombre == nombre_equipo:
                equipo.vender(cantidadvendida)
                break
        else:
            print(f"No se encontró el equipo {nombre_equipo}.")


control_stock = ControlStock()

#Propiedades de la clase
e1 = EquipoDeportivo("Pelota de voley", "2020-07-30", 30000, "Pelota de voley de alta calidad", 10000, 30000, 50)
e2 = EquipoDeportivo("Palo de jockey", "2023-15-05", 45000, "Palo de jockey mejor calidad", 32000, 45000, 35)

#Se agregan los
control_stock.agregar_equipo(e1)
control_stock.agregar_equipo(e2)

#Cantidad actual del stock
print("Equipos en stock:")
control_stock.imprimir_equipos()

#Acá es lo q se vende
control_stock.vender_equipo("Pelota de voley", 5)
control_stock.vender_equipo("Palo de jockey", 3)

#Y la cqantidad actual despues de lo q se vendió
print("Equipos en stock después de la venta:")
control_stock.imprimir_equipos()