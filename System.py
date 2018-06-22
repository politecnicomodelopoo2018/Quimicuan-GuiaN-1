from Flight import *
from Person import *
from Plane import *
import json
from Exercises import *


class System (object):

    def __init__(self):
        self.Person = []
        self.Flight = []
        self.Plane = []

    def AddPerson(self, Person):
        self.Person.append(Person)

    def AddFight(self, Flight):
        self.Flight.append(Flight)

    def AddPlane(self, Plane):
        self.Plane.append(Plane)

SystemReal = System()

Dictionary = {}

with open("Data.json", "r") as J:
    Dictionary = json.loads(J.read())




for item in Dictionary["Aviones"]:
    Planes = Plane()

    Planes.SetPlaneModel(item["codigoUnico"])
    Planes.SetMaxPassengers(item["cantidadDePasajerosMaxima"])
    Planes.SetMinCrew(item["cantidadDeTripulacionNecesaria"])

    SystemReal.AddPlane(Planes)




for item in Dictionary["Personas"]:

    if item["tipo"] == "Pasajero":
        Passengers = Passenger()

        Passengers.SetName(item["nombre"])
        Passengers.SetSurname(item["apellido"])
        Passengers.SetBirthdate(item["fechaNacimiento"])
        Passengers.SetID(item["dni"])
        Passengers.SetVIP(item["vip"])
        if "solicitudesEspeciales" in Dictionary["Personas"]:
            Passengers.AddSpecialRequest(item["solicitudesEspeciales"])

        SystemReal.AddPerson(Passengers)


    if item["tipo"] == "Piloto":
        Pilots = Pilot()

        Pilots.SetName(item["nombre"])
        Pilots.SetSurname(item["apellido"])
        Pilots.SetBirthdate(item["fechaNacimiento"])
        Pilots.SetID(item["dni"])
        for item2 in ["avionesHabilitados"]:
            Pilots.AddEnablePlane(item2)

        SystemReal.AddPerson(Pilots)


    if item["tipo"] == "Servicio":
        Services = Service()

        Services.SetName(item["nombre"])
        Services.SetSurname(item["apellido"])
        Services.SetBirthdate(item["fechaNacimiento"])
        Services.SetID(item["dni"])
        for item2 in ["avionesHabilitados"]:
            Services.AddEnablePlane(item2)
        for item3 in ["idiomas"]:
            Services.AddLanguage(item3)

        SystemReal.AddPerson(Services)




for item in Dictionary["Vuelos"]:
    Flights = Flight()

    Flights.SetPlaneModel(item["avion"])
    Flights.SetDate(item["fecha"])
    Flights.SetTime(item["hora"])
    Flights.SetOrigin(item["origen"])
    Flights.SetDestination(item["destino"])
    for item2 in ["tripulacion"]:
        Flights.AddCrew(item2)
    for item3 in ["pasajeros"]:
        for item4 in SystemReal.Person:
            if item3 == item4.ID:
                Flights.AddPassenger(item4)

    SystemReal.AddFight(Flights)


Menu = FirstExerciseClass()

for item in SystemReal.Flight:
    if item.Origin == Menu.OriginFlight:
        if item.Destination == Menu.DestinationFlight:
            for item2 in item.Passengers:
                Menu.AddPassengerFlight(item2)

for item in Menu.PassengersFlight:
    print(item)