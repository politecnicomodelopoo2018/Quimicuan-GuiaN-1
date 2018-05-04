class Pedido(object):

    Fecha = None
    Plato = None
    Persona = None
    Hora = None
    Bool = False

    def SetFecha(self,Fecha):
        self.Fecha = Fecha

    def SetPlato(self,Plato):
        self.Plato = Plato

    def SetPersona(self,Persona):
        self.Persona = Persona

    def SetHora(self,Hora):
        self.Hora = Hora

    def TrueBool(self):
        self.Bool = True

    def GetPrecioDesc(self):
         return self.Plato.Precio - self.Persona.GetDescuento() * self.Plato.Precio / 100