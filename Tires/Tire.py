from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, wear_and_tire):
        self.wear_and_tire = wear_and_tire

    @abstractmethod
    def tire_needs_serviced(self):
        pass
