from abc import ABC, abstractmethod
from battery.Battery import Battery
from engine.Engine import Engine


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.engine_needs_serviced() or self.battery.battery_needs_serviced()
