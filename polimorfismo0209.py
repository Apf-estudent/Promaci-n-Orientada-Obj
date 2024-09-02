#02/09/2024
#Actividad: crear una fabrica de calzados(?)
#Calzado: tipo,suela, made in, marca, fechadecreacion, numero
#Zapatillas: numero, modelo, materiales, stock
#faltó precio y costo

class Calzado:
    def __init__(self,made_in, tipo, suela, marca, fecha_de_creacion, numero):
        self.made_in=made_in
        self.tipo=tipo
        self.suela=suela
        self.marca=marca
        self.fecha_de_creacion=fecha_de_creacion
        self.numero=numero

    def detalles(self):
        print("__________ ______ _________")
        print("Hecho en: ",self.made_in,"\nTipo: ",self.tipo, "\nSuela :",self.suela,"\Marca: ",self.marca,"\nNúmero: ",self.numero)
        print("___ __ ___")

class Zapatilla(Calzado):
    def __init__(self, made_in,tipo, suela, marca, fecha_de_creacion, numero, numero2,modelo,materiales,stock):
        super().__init__(made_in,tipo, suela, marca, fecha_de_creacion, numero)
        self.numero2=numero2
        self.modelo=modelo
        self.materiales=materiales
        self.stock=stock
    
    def detalles(self):
        print("Número: ",self.numero2,"\nModelo: ",self.modelo,"\nMateriales: ",self.materiales,"\nStock: ",self.stock)
        print("__________ ______ _________")

T1=Calzado("Venecia","Botas","Suela de esparto","Vans","12.09.2005","37")
T1.detalles()

T2=Zapatilla("Venecia","Botas","Suela de esparto","Vans","12.09.2005","37",40,"Urbanas","Cuero eco",69)
T2.detalles()
