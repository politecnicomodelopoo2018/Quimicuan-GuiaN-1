class Persona (object):

    Nombre = None
    Apellido = None
    DNI = None
    FechaIngreso = None

    def SetNombrePersona(self, Nombre):
        self.Nombre = Nombre

    def SetApellidoPersona(self, Apellido):
        self.Apellido = Apellido

    def SetDNIPersona(self, DNI):
        self.DNI = DNI

    def SetFechaIngresoPersona(self, FechaIngreso):
        self.FechaIngreso = FechaIngreso

class Conductores(Persona):
    pass

class OperadoresTecnicos(Persona):
    pass

class Musicalizadores(Persona):
    pass