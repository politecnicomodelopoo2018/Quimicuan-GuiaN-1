from Flight import *
from Person import *
from Plane import *
import json
import datetime


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
        Passengers.SetBirthdate(datetime.datetime.strptime(item["fechaNacimiento"], "%Y-%m-%d"))
        Passengers.SetID(item["dni"])
        Passengers.SetVIP(item["vip"])
        if "solicitudesEspeciales" in item:
            Passengers.AddSpecialRequest(item["solicitudesEspeciales"])

        SystemReal.AddPerson(Passengers)


    if item["tipo"] == "Piloto":
        Pilots = Pilot()

        Pilots.SetName(item["nombre"])
        Pilots.SetSurname(item["apellido"])
        Pilots.SetBirthdate(item["fechaNacimiento"])
        Pilots.SetID(item["dni"])
        for item2 in item["avionesHabilitados"]:
            Pilots.AddEnablePlane(item2)

        SystemReal.AddPerson(Pilots)


    if item["tipo"] == "Servicio":
        Services = Service()

        Services.SetName(item["nombre"])
        Services.SetSurname(item["apellido"])
        Services.SetBirthdate(item["fechaNacimiento"])
        Services.SetID(item["dni"])
        for item2 in item["avionesHabilitados"]:
            Services.AddEnablePlane(item2)
        for item3 in item["idiomas"]:
            Services.AddLanguage(item3)

        SystemReal.AddPerson(Services)




for item in Dictionary["Vuelos"]:
    Flights = Flight()

    Flights.SetPlaneModel(item["avion"])
    Flights.SetDate(item["fecha"])
    Flights.SetTime(item["hora"])
    Flights.SetOrigin(item["origen"])
    Flights.SetDestination(item["destino"])
    for item2 in item["tripulacion"]:
        for item3 in SystemReal.Person:
            if item2 == item3.ID:
                Flights.AddCrew(item3)
    for item3 in item["pasajeros"]:
        for item4 in SystemReal.Person:
            if item3 == item4.ID:
                Flights.AddPassenger(item4)

    SystemReal.AddFight(Flights)


#ExerciseOne#

Origin = input()
Destination = input()

for item in SystemReal.Flight:
    if item.Origin == Origin:
        if item.Destination == Destination:
            for item2 in item.Passengers:
                print("---------------")
                print(item2.Name)
                print(item2.Surname)
                print(item2.Birthdate)
                print(item2.ID)

#ExerciseTwo#

Origin2 = input()
Destination2 = input()
OldPassenger = None

for item in SystemReal.Flight:
    if item.Origin == Origin2:
        if item.Destination == Destination2:
            for item2 in item.Passengers:
                if OldPassenger == None:
                    OldPassenger = item2
                if item2.Birthdate < OldPassenger.Birthdate:
                    OldPassenger = item2
            print("---------------")
            print(OldPassenger.Name)
            print(OldPassenger.Surname)
            print(OldPassenger.Birthdate)
            print(OldPassenger.ID)

#ExerciseThree#


for item in SystemReal.Flight:
    Counter = 0
    PlaneFlight = None
    for item2 in item.Crew:
        Counter+=1
    for item2 in SystemReal.Plane:
        if item2.PlaneModel == item.PlaneModel:
            PlaneFlight = item2
    if Counter < PlaneFlight.MinCrew:
        print("---------------")
        print(item.PlaneModel)
        print(item.Date)
        print(item.Time)
        print(item.Origin)
        print(item.Destination)

#ExerciseFour#


for item in SystemReal.Flight:
    for item2 in item.Crew:
        if item.PlaneModel not in item2.EnablePlanes:
            print("---------------")
            print("Unauthorized Flight")
            print(item.PlaneModel)
            print(item.Date)
            print(item.Time)
            print(item.Origin)
            print(item.Destination)
            break

#ExerciseFive#

for item in SystemReal.Person:
    DateFlight = None
    CounterFlights = 0
    if type(item) == Pilot or type(item) == Service:
        for item2 in SystemReal.Flight:
            if item in item2.Crew:
                if DateFlight == None:
                    DateFlight = item2.Date
                elif item2.Date == DateFlight:
                    CounterFlights += 1
            if CounterFlights > 0:
                print("---------------")
                print("This member of the crew is breaking the rule #420")
                print(item.Name)
                print(item.Surname)
                print(item.Birthdate)
                print(item.ID)
                break

#ExerciseSix#

for item in SystemReal.Person:
    if type(item) == Passenger:
        if item.VIP != None:
            print("---------------")
            print("This passenger is VIP")
            print(item.Name)
            print(item.Surname)
            print(item.Birthdate)
            print(item.ID)
        if len(item.SpecialRequest) != 0:
            print("---------------")
            print("This passenger has a SpecialRequest")
            print("SpecialRequest: " + item.SpecialRequest[0])
            print(item.Name)
            print(item.Surname)
            print(item.Birthdate)
            print(item.ID)

#ExerciseSeven#

for item in SystemReal.Flight:
    print("---------------")
    print(item.PlaneModel)
    print(item.Date)
    print(item.Time)
    print(item.Origin)
    print(item.Destination)
    for item2 in SystemReal.Person:
        if type(item2) == Service:
            for item3 in item2.Language:
                print(item2.ID + " Speaks " + item3)