class Plane (object):

    PlaneModel = None
    MaxPassengers = None
    MinCrew = None

    def SetPlaneModel(self, PlaneModel):
        self.PlaneModel = PlaneModel

    def SetMaxPassengers(self, MaxPassengers):
        self.MaxPassengers = MaxPassengers

    def SetMinCrew(self, MinCrew):
        self.MinCrew = MinCrew