class Plane (object):

    PlaneModel = None
    MaxPassengers = None
    MinCrew = None

    def SetPlaneModel(self, PlaneModel):
        self.PlaneModel = PlaneModel

    def SetMaxPassengers(self, MaxPassengers):
        self.MaxPassengers = int(MaxPassengers)

    def SetMinCrew(self, MinCrew):
        self.MinCrew = int(MinCrew)