class Alumno:
    def __init__(self,fullname,nota):
        self.fullname=fullname
        self.nota=nota

    def mostrar(self):
        print("Nombre: ",self.fullname,"\nNota: ",self.nota)

        if self.nota>=7:
            print("Aprobado")
        else:
            print("Reprobado")
        print("______________________________________")

A1=Alumno("Andy",8)
A1.mostrar()
A2=Alumno("Lara",3)
A2.mostrar()
A3=Alumno("Ramiro",6.5)
A3.mostrar()

            

    

