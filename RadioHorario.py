class Horario(object):

    def __init__(self):
        self.Dias = []
        self.Horas = []

    def SetDiasHorario(self, Dia):
        self.Dias.append(Dia)

    def SetHorasHorario(self, Hora):
        self.Horas.append(Hora)