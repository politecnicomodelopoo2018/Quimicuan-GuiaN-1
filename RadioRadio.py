class Radio (object):

    Nombre = None
    Frecuencia = None

    def __init__(self):
        self.Programas = []

    def SetNombreRadio(self, Nombre):
        self.Nombre = Nombre

    def SetFrecuenciaRadio(self, Frecuencia):
        self.Frecuencia = Frecuencia

    def AgregarProgramas(self, Programa):
        self.Programas.append(Programa)