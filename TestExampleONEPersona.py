class Persona(object):

    Nombre = None
    Apellido = None
    FechaNac = None

    def __init__(self):
        self.ListaRegistro = []

    def SetNombre(self, Nombre):
        self.Nombre = Nombre.title()


    def SetApellido(self, Apellido):
        self.Apellido = Apellido.title()


    def SetFechaNac(self, FechaNac):
        self.FechaNac = FechaNac.title()


    def AgregarRegistro (self, Registro):
        self.ListaRegistro.append(Registro)


    def GetRegistro (self, DiaReg, MesReg, AñoReg):
        for item in self.ListaRegistro:
            if item.DiaReg == DiaReg:
                if item.MesReg == MesReg:
                    if item.AñoReg == AñoReg:

                        return item

    def PromedioReg (self, AñoReg):
        PesoTotal = 0
        AlturaTotal = 0
        Cantidad = 0

        for item in self.ListaRegistro:

            if item.AñoReg == AñoReg:
                PesoTotal += int(item.Peso)
                AlturaTotal += float(item.Altura)
                Cantidad += 1

        return AlturaTotal/Cantidad , PesoTotal/Cantidad

    def AlturaAños (self, FirstYear, SecondYear):

        AlturaTotal1 = 0
        Cantidad1 = 0
        AlturaTotal2 = 0
        Cantidad2 = 0

        for item in self.ListaRegistro:

            if item.AñoReg == FirstYear:
                AlturaTotal1 += float(item.Altura)
                Cantidad1 += 1

            if item.AñoReg == SecondYear:
                AlturaTotal2 += float(item.Altura)
                Cantidad2 += 1

        PrimerProm = AlturaTotal1 / Cantidad1
        SegundoProm = AlturaTotal2 / Cantidad2
        PromTotal = (SegundoProm * 100 / PrimerProm)-100

        return PromTotal
