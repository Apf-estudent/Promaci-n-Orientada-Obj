#03/06/2024
#Clase de Herencia:
class Person:  #Clase Persona, es una clase padre(principal
  def __init__(self, fname, lname, fechaNacimiento, address, postalcode, dni):
    self.firstname = fname
    self.lastname = lname
    self.fechaNacimiento = fechaNacimiento
    self.address = address
    self.postalcode = postalcode
    self.dni = dni


  def printname(self):
    print(self.firstname, self.lastname, self.fechaNacimiento, self.address, self.postalcode, self.dni)


  def mostrar(self):
    print("Nombre: ",self.firstname,"\nApellido: ",self.lastname,"\nFecha de Nacimiento: ",self.fechaNacimiento)
    print(".........................")


class Student(Person):#Acá definimos como la clase Student es hija de la clase Persona
  def __init__(self, fname, lname, fechaNacimiento, address, postalcode, dni, matricula, curso, estado, año): #Polimorfismo
    super().__init__(fname, lname, fechaNacimiento, address, postalcode, dni)#"super" función que hará que la clase hija herede todos los métodos y propiedades de su clase padre

    self.matricula = matricula
    self.curso = curso
    self.estado = estado
    self.año = año


  def printname(self):
    super().printname()
    print(self.matricula, self.curso, self.estado, self.año) #Polimorfismo


  def mostrar(self):
    print("Matricula: ",self.matricula,"\nCurso: ",self.curso,"\nEstado: ",self.estado,"\nAño: ",self.año) #Polimorfismo
    print(".........................")
    return super().mostrar()
 




x1 = Student("Mike", "Olsen", "2007-01-21", "Oregon", 2025, 2019, "12345", "6to", "activo", 2019)#el "x1" es el objeto q creó la clase, al cual le pasamos las propiedades
x1.printname() #Polimorfismo

x2 = Student("Juana", "León", "2008-05-23", "Calle 1", 1234, 2020, "67890", "5to", "inactivo", 2020)
x2.printname() #Polimorfismo

x3 = Student("Pedro", "López", "2006-12-03", "Calle 2", 5678, 2021, "34567", "7mo", "activo", 2021)
x3.printname() #Polimorfismo

x4 = Student("Ana", "Martinez", "2009-06-05", "Calle 3", 9012, 2022, "23456", "3ro", "inactivo", 2022)
x4.printname() #Polimorfismo


x1.mostrar() #Polimorfismo
x2.mostrar() #Polimorfismo
x3.mostrar() #Polimorfismo
x4.mostrar() #Polimorfismo

