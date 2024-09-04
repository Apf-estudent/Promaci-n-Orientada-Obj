#28/08/2024
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
        print("_____________________________")
        print("    Rol: ESTUDIANTE")
        print("  ____ ___________ ____")
        print("Curso: ", self.curso)
        super().mostrar()
        print("_____________________________")
        
class Docentes(Escuela):
    def __init__(self, matricula, dni, fullname, adress, materias, cursoacargo):
        super().__init__(matricula, dni, fullname, adress, materias)
        self.cursoacargo=cursoacargo

    def mostrar(self):
        print("_____________________________")
        print("    Rol: DOCENTE")
        print("  ____ ___________ ____")
        print("Curso designado: ", self.cursoacargo)
        super().mostrar()
        print("_____________________________")


E1=Estudiantes(78394,"49.986.367","Antonio Hernández","Nicolás Moreno 2867","Tecnología, ciencias, arte y deporte.","4to *C*")
E1.mostrar()
E2=Estudiantes(683296,"49.832.899","Astrid Flores","Lavanda 737","Deporte, cocina, natacion, y psicología","4to *B*")
E2.mostrar()
E3=Estudiantes(94634,"49.216.533","Daniel Vnosky","Sarmiento 1083","Programación, quimica, FVT y Matematica.","4to *A*")
E3.mostrar()

D1=Docentes(64875,"25.098.687","Elías Romero","Alem 7874","Formación para la Vida y el Trabajo-FVT","4to *A*")
D1.mostrar()
D2=Docentes(89875,"22.596.987","Natalia Amor","Docente 2879","Historia","6to *D*")
D2.mostrar()
D3=Docentes(9835,"24.129.987","Nahuel Gonzalez","Ceferino Amor 7782","Educación Física","5to *B*")
D3.mostrar()
