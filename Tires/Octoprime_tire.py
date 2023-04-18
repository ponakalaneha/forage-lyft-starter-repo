from Tires.Tire import Tire


class Octoprime(Tire):
    def __init__(self, wear_and_tire):
        super().__init__(wear_and_tire)
        self.wear_and_tire = wear_and_tire

    def tire_needs_serviced(self):
        if sum(self.wear_and_tire) >= 3:
            return True
        else:
            return False
