class Registro (object):

    Peso = None
    Altura = None
    DiaReg = None
    MesReg = None
    AñoReg = None

    def SetPeso(self, Peso):
        self.Peso = Peso.title()


    def SetAltura(self, Altura):
        self.Altura = Altura.title()


    def SetDiaReg(self, DiaReg):
        self.DiaReg = DiaReg.title()


    def SetMesReg(self, MesReg):
        self.MesReg = MesReg.title()


    def SetAñoReg(self, AñoReg):
        self.AñoReg = AñoReg.title()