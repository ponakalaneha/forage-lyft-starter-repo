from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, last_serviced_date):
        self.last_serviced_date = last_serviced_date

    @abstractmethod
    def battery_needs_serviced(self):
        pass
