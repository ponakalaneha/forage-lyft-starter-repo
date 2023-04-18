from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.engine_needs_serviced() or self.battery.battery_needs_serviced() or self.tire.tire_needs_serviced()
