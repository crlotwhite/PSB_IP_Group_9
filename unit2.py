from random import randint


class Unit:
    def __init__(self, hp, a, d, e, c, ct=None):
        ''' Make an Unit for Game

        :param hp (int): Heath Point
        :param a (int): Attack Point
        :param d (int): Deffend Point
        :param e (int): Exp Point
        :param ct (CLASS_TYPE): Class Type
        '''

        self.heath_point = hp
        self.character_type = c
        self.attack_point = a
        self.defend_point = d
        self.exp = e

        print(f'Unit {id(self)} is here')

    def attack(self):
        '''randomize integer for atk, and
        deducting hp from target'''
        if (self.character_type == "warrior"):
            atk = randint(5, 20)
        elif (self.character_type == "tanker"):
            atk = randint(1, 10)
        self.choose_target() #call user target
        self.heath_point -= (self.attack_point - self.defend_point + randint(-5, 10))

    def heal(self):
        self.heath_point += 15 # assuming the fixed value for healing is 15

    def exp_calc(self):
        '''calculate exp for both the AI and the user'''
        attackerExp += totalDmg #for attacker exp
        '''for defender exp'''
        if (totalDmg > 10):
            targetExp += (self.defend_point * 1.2)
        elif (totalDmg <= 0):
            targetExp += (self.defend_point * 1.5)

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
        '''choose the lowest health point from the
        user's characters'''
        minHealth = 100
        for health in playerHealth: #playerHealth is a list for the player's characters' health
            if minHealth > health:
                minHealth = health

    def eval_self(self):
        '''check if one or more AI's character is
        dead or still alive'''
        for health in AIHealth: #AIHealth is a list of the AI's character's health
            if health <= 0:
                pass #character_state = dead
