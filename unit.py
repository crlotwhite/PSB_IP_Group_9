from random import randint
from character_types import CharacterTypes
from log_util import file_log


class Unit:
    def __init__(self, ct):
        ''' Make an Unit for Game

        :param hp (int): Heath Point
        :param e (int): Exp Point
        :param ct (CLASS_TYPE): Class Type
        '''
        self.is_dead = False
        self._health_point = 100
        self.exp = 0
        self._level = 1
        self.character_type = ct

    # Constrains the hp to not exceed 100.
    # implemented getters just in case.
    @property
    def health_point(self):
        return self._health_point

    @health_point.setter
    def health_point(self, health_point):
        # if total health point is over 100, do not any thing
        # or not if hp is under 0, just input 0
        if 100 >= health_point > 0:
            self._health_point = health_point
        elif health_point < 0:
            self._health_point = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        # do not level up more than 10.
        if level <= 10:
            self._level = level

    def hp_for_display(self):
        # make formatted str
        return f'HP: {self.health_point}/100'

    def attack(self, target):
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

    def heal(self):
        # assuming the fixed value for healing is 15
        self.health_point = self.health_point + 15
        return {
            'damage': 15,
            'exp': 0,
        }

    def do(self, *args, **kwargs):
        '''
        Unit do someting. This is Abstract Method.
        Whenever the turn comes, do() is executed.
        '''
        pass

    def eval_self(self):
        '''
        proceed unit's dead.
        '''
        if self.health_point <= 0:
            # character is dead
            self.is_dead = True


class Player(Unit):
    def __init__(self, ct):
        self.name = ''
        self.set_name()
        super().__init__(ct)

        file_log(f'Player {self.name} is created')

    def set_name(self):
        '''
        set player name from user input.
        '''

        from tkinter.simpledialog import askstring
        name = askstring('Create Character', 'What is this character\'s new name')
        self.name = name

    def do(self, *args, **kwargs):
        '''
        The main interface of the player object

        :param kwargs: ['target'] Target of attack,
                        ['state'] Chosen action
        :return: (Dict[str, any]) Data for logging
        '''

        if kwargs['state'] == 'a':
            target = kwargs['target']
            result = self.attack(target)
        elif kwargs['state'] == 'h':
            result = self.heal()

        self.eval_self()
        return {
            'name': self.name,
            'action': kwargs['state'],
            'target': target.name if kwargs.get('target') else 'itself',
            'damage': result['damage'], # atk or heal
            'exp': result['exp'],
        }


class AI(Unit):
    def __init__(self, ct):
        self.name = 'AI' + str(randint(10, 99))
        super().__init__(ct)

    def do(self, *args, **kwargs):
        '''
        :param kwargs: ['player_list']
        :return:
        '''
        target = AI.lowest_hp_player(kwargs['player_list'])
        state = self.choose_state(kwargs['player_list'], target.health_point)
        if state == 'a':
            result = self.attack(target)
        elif state == 'h':
            result = self.heal()

        self.eval_self()
        return {
            'name': self.name,
            'action': state,
            'target': target.name if state == 'a' else 'itself',
            'damage': result['damage'],  # atk or heal
            'exp': result['exp'],
        }

    def choose_state(self, player_list, lowest_player_hp):
        '''
        Choose the action of the AI.

        :param player_list: (List[Player]) Player list
        :param lowest_player_hp: (Player) The weakest player's health
        :return: (str)
            a signal is attack
            h signal is heal
        '''

        # Weight for power recovery
        weight = 0

        if self.health_point == 100:
            # No need to recover stamina
            return 'a'
        elif self.health_point > 85:
            weight += 2
        elif self.health_point > 50:
            weight += (100 - self.health_point)

        ct_ratio = AI.player_class_type_ratio(player_list)
        if self.health_point < ct_ratio:
            weight += 25
        elif self.health_point == ct_ratio:
            weight += 15
        elif self.health_point > ct_ratio:
            weight += 5

        if lowest_player_hp >= 20:
            weight += lowest_player_hp

        # create random value
        random = randint(1, 130)  # the 130 value is the maximum chance value
        if random <= weight:
            return 'h'
        else:
            return 'a'

    @staticmethod
    def player_class_type_ratio(player_list):
        '''Measures the average maximum attack power for each class.'''
        result = 0
        for player in player_list:
            if player.is_dead:
                continue

            if player.character_type == CharacterTypes.warrior.value:
                result += 20
            elif player.character_type == CharacterTypes.tanker.value:
                result += 10

        return result // 3

    @staticmethod
    def lowest_hp_player(player_list):
        weak_player = player_list[0]

        for player in player_list:
            if 5 < abs(player.health_point - weak_player.health_point) < 10:
                if randint(1, 4) == 3:
                    weak_player = player
            elif player.health_point < weak_player.health_point:
                weak_player = player
            elif player.health_point == weak_player.health_point:
                if player.character_type == CharacterTypes.warrior.value:
                    weak_player = player

        return weak_player



