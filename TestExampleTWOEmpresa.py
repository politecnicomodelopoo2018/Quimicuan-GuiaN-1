from TestExampleTWORegistro import Registro
from datetime import date

Registro = Registro()

class Empresa (object):

    def __init__(self):
        self.ListaEmpleados = []

    def Llamada(self, NumeroOG, NumeroDT):

        for item in self.ListaEmpleados:

            if item.NumTelefono == NumeroOG:

                for item1 in self.ListaEmpleados:

                    if item1.NumTelefono == NumeroDT:

                        Registro.AgregarOG(item)
                        Registro.AgregarDT(item1)
                        Fecha = input() #DD/MM/YYYY
                        Registro.AgregarFecha(Fecha)

                        return True

        return False

    def Colgar(self, Duracion):
        Registro.AgregarDuracion(Duracion)


