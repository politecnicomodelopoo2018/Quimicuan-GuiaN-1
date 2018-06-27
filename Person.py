class Person (object):

    Name = None
    Surname = None
    Birthdate = None
    ID = None

    def SetName(self, Name):
        self.Name = Name

    def SetSurname(self, Surname):
        self.Surname = Surname

    def SetBirthdate(self, Birthdate):
        self.Birthdate = Birthdate

    def SetID(self, ID):
        self.ID = str(ID)

class Passenger (Person):

    VIP = None

    def SetVIP(self, VIP):
        self.VIP = VIP

    def __init__(self):
        self.SpecialRequest = []

    def AddSpecialRequest(self, SpecialRequest):
        self.SpecialRequest.append(SpecialRequest)

class Crew (Person):

    def __init__(self):
        self.EnablePlanes = []

    def AddEnablePlane(self, PlaneModel):
        self.EnablePlanes.append(PlaneModel)

class Pilot (Crew):
    pass

class Service (Crew):

    def __init__(self):
        super().__init__()
        self.Language = []

    def AddLanguage(self, Language):
        self.Language.append(Language)