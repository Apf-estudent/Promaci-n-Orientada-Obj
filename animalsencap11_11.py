class Animal:
  def __init__ (self,nombre, edad, raza, historial,datosDuenios) :
      self.nombre=nombre
      self.edad=edad
      self.raza=raza
      self.__historial=historial
      self.datosDuenios=datosDuenios

  def verInfo(self): #Método público que va a poder llamar las funciones privadas q se encuentren en la función
    self.__mostrar() #__mostrar es un método privado q no va a ser accesible para el exterior
#verInfo va a poder llamar a este método, pero las demás funciones no lo van a poder hacer por ser externas
  def __mostrar(self): 
    print(f"Nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}, historial: {self.__historial}, datosDuenios: {self. datosDuenios}")

class Gato(Animal):
 def __init__ (self,nombre, edad, raza, historial,datosDuenios,orejas,cola, unias):
  super().__init__ (nombre, edad, raza, historial,datosDuenios)
  self.orejas=orejas
  self.cola=cola
  self.unias=unias

 def verInfo(self):
   super().verInfo()
   self.__mostrar()

 def __mostrar(self):
   print(f"Orejas: {self.orejas }, Cola: {self.cola}, Unias: {self.unias}")


a1=Animal("Pepe",2,"Belga","Garrapatas","Juan telefon: 304945855")
#a1.__mostrar por ejemplo nos va a dar error al ser un método privado
#Entonces lo tenemos q llamar desde su función pública que seria "verInfo"
a1.verInfo()
g1=Gato("Pepito",2,"Siames","Garrapatas y pulgas", "Juana teléfono: 304945345", 2, 1, "Filosas" )
g1.verInfo()
