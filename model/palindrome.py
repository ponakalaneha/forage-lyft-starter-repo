from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, indicator, last_serviced_date):
        self.engine = SternmanEngine(indicator)
        self.battery = SpindlerBattery(last_serviced_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()
