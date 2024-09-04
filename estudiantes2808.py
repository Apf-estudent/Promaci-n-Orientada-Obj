#--Actividad 2--
#Crear un programa que contenga los datos personales de personas que forman parte de una escuela: estudiantes y docentes.
#Deberas identificar los siguientes atributos y aplicarlos a Clases en POO: matricula, dni, nombreApellido, direccion, anioCurso, materias, cursosAcargo. 
#crear funciones para mostrar sus datos. 
#Crear 3 objetos para cada clase

class Escuela:
    def __init__(self, matricula, dni, fullname, adress, materias):
        self.matricula=matricula
        self.dni=dni
        self.fullname=fullname
        self.adress=adress
        self.materias=materias

    def mostrar(self):
        print("Matrícula: ",self.matricula,"\nD.N.I: ",self.dni,"\nNombre completo: $",self.fullname,"\nDirección: ",self.adress,"\nMaterias: ",self.materias)

class Estudiantes(Escuela):
    def __init__(self, matricula, dni, fullname, adress, materias, curso):
        super().__init__(matricula, dni, fullname, adress, materias)
        self.curso=curso

    def mostrar(self):
        print("Rol: Estudiante")
        print("Curso: ", self.curso)
        super().mostrar()
        print("_____________________________")
        
class Docentes(Escuela):
    def __init__(self, matricula, dni, fullname, adress, materias, cursoacargo):
        super().__init__(matricula, dni, fullname, adress, materias)
        self.cursoacargo=cursoacargo

    def mostrar(self):
        print("Rol: Docente")
        print("Curso designado: ", self.cursoacargo)
        super().mostrar()
        print("_____________________________")


E1=Estudiantes(78394,"49.986.367","Antonio Hernández","Nicolás Moreno 2867","Tecnología, ciencias, arte y deporte.","4to *C*")
E1.mostrar()

D1=Docentes(64875,"25.098.687","Elías Romero","Alem 7874","Formación para la Vida y el Trabajo-FVT","4to *A*")
D1.mostrar()
