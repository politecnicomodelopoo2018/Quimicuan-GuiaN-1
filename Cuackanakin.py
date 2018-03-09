class Alumno(object):
    Nombre = None
    Apellido = None

    def SetNombre(self, Nombre):
        self.Nombre = Nombre.title()

    def GetNombre(self):
        return self.Nombre

    def SetApellido(self, Apellido):
        self.Apellido = Apellido.title()

    def GetApellido(self):
        return self.Apellido

Alumno = Alumno()
Nombre = input("Ingresar Nombre ")
Apellido = input("Ingresar Apellido ")

Alumno.SetNombre(Nombre)
Alumno.SetApellido(Apellido)

print(Alumno.GetApellido(), end = "")
print(", ", end = "")
print(Alumno.GetNombre())