class Flight (object):

    PlaneModel = None
    Date = None
    Time = None
    Origin = None
    Destination = None

    def __init__(self):
        self.Passengers = []
        self.Crew = []

    def SetPlaneModel(self, PlaneModel):
        self.PlaneModel = PlaneModel

    def SetDate(self, Date):
        self.Date = Date

    def SetTime(self, Time):
        self.Time = Time

    def SetOrigin(self, Origin):
        self.Origin = Origin

    def SetDestination(self, Destination):
        self.Destination = Destination

    def AddPassenger(self, Passenger):
        self.Passengers.append(Passenger)

    def AddCrew(self, Crew):
        self.Crew.append(Crew)