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

class Estudiantes(Escuela):
    def __init__(self, curso):
        super()
        self.curso=curso

    def mostrar()
        
class Docentes(Escuela):
    def __init__(self, cursoacargo):
        super()
        self.cursoacargo=cursoacargo
