from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self, current_mileage, last_serviced_mileage, last_serviced_date):
        self.engine = WilloughbyEngine(current_mileage, last_serviced_mileage)
        self.battery = SpindlerBattery(last_serviced_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()
