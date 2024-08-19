
class AnimalMarino:
     def __init__(self, nombre, largo, especie, peso, vida):
         self.nombre = nombre
         self.largo = largo
         self.especie = especie
         self.peso = peso
         self.vida = vida

     def mostrar(self):
        print(".........................")
        print("Nombre: ",self.nombre,"\nLargo: ",self.largo,"\nEspecie:",self.especie,"\nPeso: ", self.peso,"\nPromedio de vida: ",self.vida)
        print(".........................")
        print("")

Animal1=AnimalMarino("Orca","6 a 8 metros","Cetaceo Odontoceo","3.000kg a 4.000kg","50 a 90 años")
Animal2=AnimalMarino("Tiburón Toro","3 a 5 metros","Condrictios","130kg u 95kg","35 años")
Animal3=AnimalMarino("Beluga","4 metros","D. Leucas, Pallas","1.200kg o 1.600kg","35 a 50 años")
Animal4=AnimalMarino("Calamar Gigante","4.5 metros","Decapodiformes","120 a 150kg","9 meses a 5 años")

Animal1.mostrar()
Animal2.mostrar()
Animal3.mostrar()
Animal4.mostrar()

