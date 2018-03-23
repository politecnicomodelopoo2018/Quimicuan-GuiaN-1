import datetime

Now = datetime.datetime.now()


class Empleado(object):
    Nombre = None
    Apellido = None
    Telefono = None
    FechaNac = None

    def __init__(self):
        self.DiasLaburo = []
        self.DiasAsistencia = []

    def SetNombre(self, Nombre):
        self.Nombre = Nombre.title()

    def SetApellido(self, Apellido):
        self.Apellido = Apellido.title()

    def SetTelefono(self, Telefono):
        self.Telefono = Telefono.title()

    def SetFechaNac(self, FechaNac):
        self.FechaNac = FechaNac.title()

    def SetDiasLaburo(self, Dia):
        self.DiasLaburo.append(Dia)

    def SetDiasAsistencia(self):
        self.DiasAsistencia.append(Now.year + Now.month + Now.day + Now.hour)

    def GetPorcentajeAsistencia(self, Año, Mes):
        DiasVino = 0
        for item in self.DiasAsistencia:
            if item == Año:
                if item == Mes:
                    if item == self.DiasLaburo:
                        DiasVino + 1
        PorcentajeDeAsistencia = DiasVino / 30
        return PorcentajeDeAsistencia
