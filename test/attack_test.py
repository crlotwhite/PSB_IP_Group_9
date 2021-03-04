import unittest
from unittest.mock import patch

from unit import Unit
from character_types import CharacterTypes


class MockUnit(Unit):
    # Since it is impossible to mock the methods of other classes,
    # we override them with copy paste and use the same as possible.
    @patch('random.randint', return_value=5)
    def attack(self, target, randint):
        '''randomize integer for atk, and deducting hp from target'''

        # random attack point depending on class type.
        if self.character_type == CharacterTypes.warrior.value:
            attack_point = randint(5, 20)
        elif self.character_type == CharacterTypes.tanker.value:
            attack_point = randint(1, 10)

        # random defend point depending on class type.
        if target.character_type == CharacterTypes.tanker.value:
            defend_point = randint(5, 15)
        elif target.character_type == CharacterTypes.warrior.value:
            defend_point = randint(1, 10)

        # calculate total damage.
        total_damage = attack_point - defend_point + randint(-5, 10)

        # if total damage is negative, do not any thing.
        if total_damage > 0:
            target.health_point = target.health_point - total_damage

        # after attack, calculate exp for both the AI and the user
        if total_damage > 0:
            self.exp = self.exp + (total_damage * 10)  # for attacker exp

        # for defender exp
        if total_damage > 10:
            target.exp += (defend_point * 1.2)
        elif total_damage <= 0:
            target.exp += (defend_point * 1.5)

        # proceed level
        while (self.exp // 100) > 0:
            self.exp -= 100
            self.level = self.level + 1

        while (target.exp // 100) > 0:
            target.exp -= 100
            target.level = target.level + 1

        # return message
        if total_damage > 0:
            return {
                'damage': total_damage,
                'exp': total_damage,
            }
        else:
            return {
                'damage': 0,
                'exp': 0,
            }


class AttackTest(unittest.TestCase):
    def setUp(self):
        self.u1 = MockUnit('warrior')
        self.u2 = MockUnit('warrior')

    def test_general_attack_test(self):
        # Since we fixed the value of randint at 5, we have 5 health damage and 50 experience.
        self.u1.attack(self.u2)

        self.assertEqual(self.u2.health_point, 95)
        self.assertEqual(self.u1.exp, 50)

    def test_kill_test(self):
        self.u2.health_point = 5
        self.u1.attack(self.u2)
        self.u2.eval_self()
        self.assertTrue(self.u2.is_dead)


if __name__ == '__main__':
    unittest.main()
