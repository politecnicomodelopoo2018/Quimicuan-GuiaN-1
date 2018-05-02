class Persona(object):

    Nombre = None
    Apellio = None

    def SetNombre(self, Nombre):
        self.Nombre = Nombre

    def SetApellido(self,Apellido):
        self.Apellio = Apellido

class Alumno(Persona):

    Division = None

    def SetDivision(self,Division):
        self.Division = Division

class Profesor(Persona):

    Descuento = None

    def SetDescuento(self,Descuento):
        self.Descuento = Descuento