#12/08/2024
#Polimorfismo
class Notas:
    def __init__(self, fname, nota1, nota2, nota3):
        self.fname=fname
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3

    def nombre(self):
        print("Nombre: ", self.fname)

    def mostrar(self):
        print("Primera nota: ", self.nota1)
        print("Segunda nota: ", self.nota2)
        print("Tercera nota: ", self.nota3)
        print("________")

    def notasort(self):
        notas = [self.nota1, self.nota2,self.nota3]
        notas.sort(reverse=True)#".sort" clasifica las notas | "reverse=true" de mayor a menor
        return notas

#Primer Alumno
A1=Notas("Gabriel", 8, 9,8.5)
A1.nombre()
notas_ordenadas=A1.notasort()
print("Mejores notas: ", notas_ordenadas)
A1.mostrar()

#Segundo Alumno
A2=Notas("Fernando",5,10,7)
A2.nombre()
notas_ordenadas=A2.notasort()
print("Mejores notas: ", notas_ordenadas)
A2.mostrar()
