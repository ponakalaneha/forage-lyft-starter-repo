from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, current_mileage, last_serviced_mileage, last_serviced_date):
        self.engine = CapuletEngine(current_mileage, last_serviced_mileage)
        self.battery = NubbinBattery(last_serviced_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()
