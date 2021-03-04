import unittest

from unit import Unit


class HealthPointPropertyTest(unittest.TestCase):
    def setUp(self):
        '''It runs before each test is run.'''
        self.u1 = Unit('warrior')

    def test_basic_input_and_output(self):
        self.u1.health_point = 50
        self.assertEqual(self.u1.health_point, 50)

    def test_enter_a_number_greater_than_100(self):
        self.u1.health_point = 110
        self.assertEqual(self.u1.health_point, 100)

    def test_handling_negative_number_input(self):
        self.u1.health_point = -10
        self.assertEqual(self.u1.health_point, 0)


class LevelPropertyTest(unittest.TestCase):
    def setUp(self):
        self.u1 = Unit('warrior')

    def test_basic_input_and_output(self):
        self.u1.level = 4
        self.assertEqual(self.u1.level, 4)

    def maximum_level_limit_test(self):
        self.u1.level = 15
        self.assertEqual(self.u1.level, 10)


if __name__ == '__main__':
    unittest.main()
