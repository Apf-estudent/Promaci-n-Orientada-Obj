class ClubdeDeportes:
    def __init__(self,deporte,jugadores,espacio):
        self.deporte= deporte
        self.jugadores= jugadores
        self.espacio= espacio

    def mostrar(self):
        print(".........................")
        print("Deporte: ",self.deporte,"\nCantidad de Jugadores: ",self.jugadores,"\nEspacio de Juego:",self.espacio,)
        print(".........................")
        print("")


Deporte1=ClubdeDeportes("Voley.","6 por equipo.","Cancha con red.")
Deporte2=ClubdeDeportes("Fútbol.","11 por equipo y 3 suplentes.","Cancha con arco.")
Deporte3=ClubdeDeportes("Tenis","2 jugadores/as (individuales) o entre dos parejas (dobles).","Cancha con red en medio,")


Deporte1.mostrar()
Deporte2.mostrar()
Deporte3.mostrar()