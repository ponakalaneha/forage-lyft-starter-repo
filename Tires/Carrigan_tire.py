from Tires.Tire import Tire


class Carrigan(Tire):
    def __init__(self, wear_and_tire):
        super().__init__(wear_and_tire)
        self.wear_and_tire = wear_and_tire

    def tire_needs_serviced(self):
        if max(self.wear_and_tire) >= 0.9:
            return True
        else:
            return False
