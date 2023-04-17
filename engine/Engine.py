from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, current_mileage, last_serviced_mileage, indicator):
        self.current_mileage = current_mileage
        self.last_serviced_mileage = last_serviced_mileage
        self.indicator = indicator

    @abstractmethod
    def engine_needs_serviced(self):
        pass
