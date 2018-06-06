from .Flight import Flight
from .Person import Person
from .Plane import Plane
import json

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