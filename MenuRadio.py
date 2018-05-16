from .RadioRadio import Radio
from .RadioPrograma import Programa
from .RadioPrograma import ProgramaMusica
from .RadioHorario import Horario
from .RadioPersona import OperadoresTecnicos
from .RadioPersona import Conductores
from .RadioPersona import Musicalizadores
from .SistemaRadio import Sistema

class Menu (object):

    @classmethod

    def Menu(cls, Opcion):

        Sistema1 = Sistema()

        if Opcion == 0:     ##CreadorRadios
            Radio1 = Radio()

            Radio1.SetNombreRadio(str(input()))
            Radio1.SetFrecuenciaRadio(int(input()))

        if Opcion == 1:     ##CreadorConductores
            Conductor = Conductores()

            Conductor.SetNombrePersona(str(input()))
            Conductor.SetApellidoPersona(str(input()))
            Conductor.SetDNIPersona(int(input()))
            Conductor.SetFechaIngresoPersona(str(input()))

            Sistema1.Persona.append(Conductor)

        if Opcion == 2:     ##CreadorOperadoresTecnicos
            Operador = OperadoresTecnicos()

            Operador.SetNombrePersona(str(input()))
            Operador.SetApellidoPersona(str(input()))
            Operador.SetDNIPersona(int(input()))
            Operador.SetFechaIngresoPersona(str(input()))

            Sistema1.Persona.append(Operador)

        if Opcion == 3:     ##CreadorMusicalizador
            Musicalizador = Musicalizadores()

            Musicalizador.SetNombrePersona(str(input()))
            Musicalizador.SetApellidoPersona(str(input()))
            Musicalizador.SetDNIPersona(int(input()))
            Musicalizador.SetFechaIngresoPersona(str(input()))

            Sistema1.Persona.append(Musicalizador)

        if Opcion == 4:     ##CreadorHorario
            Horario1 = Horario()

            Horario1.SetDiasHorario(str(input()))
            Horario1.SetHorasHorario(int(input()))

            Sistema1.Horarios.append(Horario1)

        if Opcion == 5:     ##CreadorPrograma