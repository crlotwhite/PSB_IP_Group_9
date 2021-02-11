from random import randint


class Unit:
    def __init__(self, hp, a, d, e, ct=None):
        ''' Make an Unit for Game

        :param hp (int): Heath Point
        :param a (int): Attack Point
        :param d (int): Deffend Point
        :param e (int): Exp Point
        :param ct (CLASS_TYPE): Class Type
        '''

        self.heath_point = hp
        self.attack_point = a
        self.defend_point = d
        self.exp = e

        print(f'Unit {id(self)} is here')

    def attack(self):
        pass

    def heal(self):
        pass

    def exp_calc(self):
        pass

    def choose_target(self):
        pass


class Player(Unit):
    def __init__(self, hp, a, d, e, ct=None):
        self.name = ''
        self.set_name()
        super().__init__(hp, a, d, e, ct)

        print(f'Player {self.name} is here')

    def set_name(self):
        '''
        set player name from user input.
        '''

        name = input('What is this character\'s new name')
        self.name = name

    def choose_target(self):
        pass


class AI(Unit):
    def __init__(self, hp, a, d, e, ct=None):
        self.name = 'AI' + str(randint(10, 99))
        super().__init__(hp, a, d, e, ct)

        print(f'AI {self.name} is here')

    def do(self, state):
        pass

    def choose_target(self):
        pass

    def eval_self(self):
        pass

