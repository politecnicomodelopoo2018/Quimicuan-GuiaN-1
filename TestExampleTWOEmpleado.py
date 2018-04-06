class Empleado(object):

    Nombre = None
    Apellido = None
    DNI = None
    Pais = None
    NumTelefono = None

    def SetNombre(self, Nombre):
        self.Nombre = Nombre.title()

    def SetApellido(self, Apellido):
        self.Apellido = Apellido.title()

    def SetDNI(self, DNI):
        self.DNI = DNI.title()

    def SetPais(self, Pais):
        self.Pais = Pais.title()

    def SetNumTelefono(self, NumTel):
        self.NumTelefono = NumTel.title()
