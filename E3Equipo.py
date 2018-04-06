class Equipo(object):
    Nombre = None
    Barrio = None
    Mañana = None
    Tarde = None
    Noche = None

    def __init__(self):
        self.ListaJugadores = []

    def DefEquipo(self, Nombre, Barrio, Mañana, Tarde, Noche):
        self.Nombre = Nombre
        self.Barrio = Barrio
        self.Mañana = Mañana
        self.Tarde = Tarde
        self.Noche = Noche

    def AgregarJugador(self, unJugador):
        if len(self.ListaJugadores) == 10:
            return 0
        else:
            self.ListaJugadores.append(unJugador)


