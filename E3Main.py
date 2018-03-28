from E3Torneo import Campeonato
from E3Equipo import Equipo
from E3Jugadores import Jugador

Liga = Campeonato()

Team = Equipo()

print("Ingresar Nombre del equipo")
NombreEquipo = input()

print("Ingresar Barrio del equipo")
Barrio = input()

print("Ingresar Mañana del equipo")
if input() == "S":
    Mañana = True
else:
    Mañana = False


print("Ingresar Tarde del equipo")
if input() == "S":
    Tarde = True
else:
    Tarde = False

print("Ingresar Noche del equipo")
if input() == "S":
    Noche = True
else:
    Noche = False

Team.DefEquipo(NombreEquipo, Barrio, Mañana, Tarde, Noche)

Player = Jugador()
Vueltas = 0
CantJug = 10

for Vueltas in range(CantJug):

    print("Ingresar Nombre del jugador")
    Nombre = input()

    print("Ingresar FechaDeNacimiento del jugador")
    FechaNac = input()

    print("Ingresar Numero del jugador")
    Numero = input()

    print("El jugador es capitan? S/N")
    if input() == "S":
        Capitan = True
    else:
        Capitan = False

    Player.AnotarJugador(Nombre, FechaNac, Numero, Capitan)

    Team.AgregarJugador(Player)

for item in Equipo.ListaJugadores:
    print(item.Nombre)