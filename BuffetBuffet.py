from BuffetPersona import Alumno
from BuffetPersona import Profesor
from BuffetPlato import Plato

class Buffet(object):

    def __init__(self):
        self.plato = []
        self.Persona = []
        self.Pedido = []

    def TxtPersona(self):

        f = open("Texto.Persona", "w")
        for item in self.Persona:
            x = item.__class__.__name__

            if type(item) is Alumno:
                f.write(x + "|" + item.Nombre + "|" + item.Apellido + "|" + item.Division + "|" + "\n")

            elif type(item) is Profesor:
                f.write(x + "|" + item.Nombre + "|" + item.Apellido + "|" + item.Descuento + "|" + "\n")

        f.close()

    def CargarPersona(self):

        f = open("Texto.Persona", "r")
        for line in f:

            Datos=line.split("|")
            print(Datos)

            if Datos[0] == "Alumno":

                Jorges = Alumno()

                Jorges.SetNombre(Datos[1])

                Jorges.SetApellido(Datos[2])

                Jorges.SetDivision(Datos[3])

                self.Persona.append(Jorges)

            if Datos[0] == "Profesor":

                Pruchis = Profesor()

                Pruchis.SetNombre(Datos[1])

                Pruchis.SetApellido(Datos[2])

                Pruchis.SetDescuento(Datos[3])

                self.Persona.append(Pruchis)


    def TxtPlato(self):

        f = open("Texto.Plato", "w")
        for item in self.plato:

            f.write(item.Nombre + "|" + str(item.Precio) + "|" + "\n")

        f.close()

    def CargarPlato(self):

        f = open("Texto.Plato", "r")
        for line in f:

            Datos=line.split("|")
            print(Datos)

            Plato2 = Plato()

            Plato2.SetNombre(Datos[0])

            Plato2.SetPrecio(Datos[1])

            self.plato.append(Plato2)