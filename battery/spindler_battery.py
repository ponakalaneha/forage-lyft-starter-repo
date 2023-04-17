from datetime import datetime
from battery.Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_serviced_date):
        super().__init__(last_serviced_date)
        self.last_serviced_date = last_serviced_date

    def battery_needs_serviced(self):
        return self.last_serviced_date.replace(year=self.last_serviced_date.year + 2) < datetime.today().date()