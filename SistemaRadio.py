from .RadioRadio import Radio
from .RadioPrograma import Programa
from .RadioPrograma import ProgramaMusica
from .RadioHorario import Horario
from .RadioPersona import OperadoresTecnicos
from .RadioPersona import Conductores
from .RadioPersona import Musicalizadores

class Sistema(object):

    def __init__(self):
        self.Radios = []
        self.Programas = []
        self.Persona = []
        self.Horarios = []