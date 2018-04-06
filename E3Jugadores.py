class Jugador(object):
    Nombre = None
    FechaNac = None
    Numero = None
    Capitan = None

    def AnotarJugador(self, Nombre, FechaNac, Numero, Capitan):
        self.Nombre = Nombre
        self.FechaNac = FechaNac
        self.Numero = Numero
        self.Capitan = Capitan