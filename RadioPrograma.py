class Programa(object):

    Horario = None
    Nombre = None
    OperadorTecnico = None
    Categoria = None

    def __init__(self):
        self.Conductores = []

    def SetHorarioPrograma(self, Horario):
        self.Horario = Horario

    def SetNombrePrograma(self, Nombre):
        self.Nombre = Nombre

    def SetTecnicosPrograma(self, Tecnico):
        self.OperadorTecnico = Tecnico

    def SetCategoriaPrograma(self, Categoria):
        self.Categoria = Categoria


    def AgregarConductores(self, Conductores):
        self.Conductores.append(Conductores)

class ProgramaMusica (Programa):

    Musicalizador = None
    EstiloDeMusica = None

    def SetMusicalizadorProgramaMusica(self, Musicalizador):
        self.Musicalizador = Musicalizador

    def SetEstiloProgramaMusica(self, Estilo):
        self.EstiloDeMusica = Estilo