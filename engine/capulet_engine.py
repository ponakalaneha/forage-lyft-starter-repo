from engine.Engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_serviced_mileage):
        super().__init__(current_mileage, last_serviced_mileage, False)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_serviced_mileage

    def engine_needs_serviced(self):
        return self.current_mileage - self.last_serviced_mileage > 30000
