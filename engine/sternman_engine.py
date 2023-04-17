from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, indicator):
        super().__init__(0, 0, indicator)
        self.indicator = indicator

    def engine_needs_serviced(self):
        if self.indicator:
            return True
        else:
            return False
