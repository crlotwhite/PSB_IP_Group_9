import unittest

from unit import Unit
from game_manager import GameManager


class MockGameManager(GameManager):
    def __init__(self):
        self.player_slot = [Unit('warrior') for _ in range(3)]
        self.ai_slot = [Unit('warrior') for _ in range(3)]


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.gm = MockGameManager()

    def test_player_win(self):
        for unit in self.gm.ai_slot:
            unit.is_dead = True

        self.assertTrue(self.gm.is_player_win())

    def test_plater_lose(self):
        for unit in self.gm.player_slot:
            unit.is_dead = True

        self.assertTrue(self.gm.is_ai_win())


if __name__ == '__main__':
    unittest.main()
