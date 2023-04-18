import unittest
from Tires.Carrigan_tire import Carrigan


class TestCarrigan(unittest.TestCase):
    def test_Tire_should_be_serviced(self):
        # test_case
        wear_and_tire = [0.9, 0.1, 0.1, 0.1]
        # Instances
        tire = Carrigan(wear_and_tire)
        # verification
        self.assertTrue(tire.tire_needs_serviced())

    def test_Tire_should_not_be_serviced(self):
        wear_and_tire = [0.4, 0.1, 0.1, 0.1]
        tire = Carrigan(wear_and_tire)
        self.assertFalse(tire.tire_needs_serviced())
