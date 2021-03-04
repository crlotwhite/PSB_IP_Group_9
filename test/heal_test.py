import unittest

from unit import Unit


class HealTest(unittest.TestCase):
    def setUp(self):
        self.u1 = Unit('warrior')

    def test_something(self):
        self.u1.health_point = 5
        self.u1.heal()
        self.assertEqual(self.u1.health_point, 20)

    def test_is_overheal(self):
        self.u1.health_point = 95
        self.u1.heal()
        self.assertEqual(self.u1.health_point, 100)


if __name__ == '__main__':
    unittest.main()
