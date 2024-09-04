class AnimalMarino:

  def __init__(animal, nombre, largo, tipo):
    animal.nombre = nombre
    animal.largo = largo
    animal.tipo = tipo
    
  def mostrar(animal):
      print("Animal: ", animal.nombre, "\nTamaño: ", animal.largo,"\nTipo: ", animal.tipo)

a1 = AnimalMarino("Orca", "6 a 8 metros", "acuático")
a1.mostrar()
