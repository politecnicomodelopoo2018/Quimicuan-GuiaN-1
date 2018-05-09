from BuffetPersona import Alumno
from BuffetPersona import Profesor

class Buffet(object):

    def __init__(self):
        self.plato = []
        self.Persona = []
        self.Pedido = []

    def TxtPersona(self):
        for item in self.Persona:
            if type(item) is Alumno:
                f = open("Texto.Persona", "w")
                f.write(item.Nombre + "|" + item.Apellido + "|" + item.Division + "\n")
                f.close()
            if type(item) is Profesor:
                f = open("Texto.Persona", "w")
                f.write(item.Nombre + "|" + item.Apellido + "|" + item.Descuento + "\n")
                f.close()
