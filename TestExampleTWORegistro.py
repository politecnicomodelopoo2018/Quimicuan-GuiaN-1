class Registro(object):

    def __init__(self):
        self.EmpleadoOG = []
        self.EmpleadoDT = []
        self.FechaCall = []
        self.DuracionCall = []

    def AgregarOG(self, Empleado):
        self.EmpleadoOG.append(Empleado)

    def AgregarDT(self, Empleado):
        self.EmpleadoDT.append(Empleado)

    def AgregarFecha(self, Fecha):
        self.FechaCall.append(Fecha)

    def AgregarDuracion(self, Duracion):
        self.DuracionCall.append(Duracion)