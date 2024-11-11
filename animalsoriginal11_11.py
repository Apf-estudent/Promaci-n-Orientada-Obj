class Animal:
  def __init__ (self,nombre, edad, raza, historial,datosDuenios) :
      self.nombre=nombre
      self.edad=edad
      self.raza=raza
      self.historial=historial
      self.datosDuenios=datosDuenios

  def mostrar(self):
    print(f"Nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}, historial: {self.historial}, datosDuenios: {self. datosDuenios}")

class Gato(Animal):
 def __init__ (self,nombre, edad, raza, historial,datosDuenios,orejas,cola, unias):
  super().__init__ (nombre, edad, raza, historial,datosDuenios)
  self.orejas=orejas
  self.cola=cola
  self.unias=unias

 def mostrar(self):
   super().mostrar()
   print(f"Orejas: {self.orejas }, Cola: {self.cola}, Unias: {self.unias}")


a1=Animal("Pepe",2,"Belga","Garrapatas","Juan telefon: 304945855")
a1.mostrar()
g1=Gato("Pepito",2,"Siames","Garrapatas y pulgas", "Juana teléfono: 304945345", 2, 1, "Filosas" )
g1.mostrar()
