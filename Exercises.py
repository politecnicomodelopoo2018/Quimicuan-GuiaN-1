class FirstExerciseClass(object):

    OriginFlight = input()
    DestinationFlight = input()

    def __init__(self):
            self.PassengersFlight = []

    def AddPassengerFlight(self, PassengerFlight):
        self.PassengersFlight.append(PassengerFlight)