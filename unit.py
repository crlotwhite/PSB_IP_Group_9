from random import randint
from character_types import CharacterTypes


class Unit:
    def __init__(self, ct):
        ''' Make an Unit for Game

        :param hp (int): Heath Point
        :param e (int): Exp Point
        :param ct (CLASS_TYPE): Class Type
        '''
        self.is_dead = False
        self.heath_point = 100
        self.exp = 0
        self.level = 1
        self.character_type = ct

        print(f'Unit {id(self)} is here')

    def attack(self, target):
        '''randomize integer for atk, and deducting hp from target'''
        if self.character_type == CharacterTypes.warrior:
            attack_point = randint(5, 20)
        elif self.character_type == CharacterTypes.tanker:
            attack_point = randint(1, 10)

        if target.character_type == CharacterTypes.tanker:
            defend_point = randint(5, 15)
        elif target.character_type == CharacterTypes.warrior:
            defend_point = randint(1, 10)

        total_damage = attack_point - defend_point + randint(-5, 10)
        target.heath_point -= total_damage

        #after attack, calculate exp for both the AI and the user
        self.exp += total_damage  # for attacker exp

        #for defender exp
        if total_damage > 10:
            target.exp += (defend_point * 1.2)
        elif total_damage <= 0:
            target.exp += (defend_point * 1.5)

        # proceed level
        while (self.exp // 100) > 0:
            self.exp -= 100
            self.level += 1

    def heal(self):
        self.heath_point += 15  # assuming the fixed value for healing is 15

    def choose_target(self):
        ''' Choose Target for Attack. this is Abstract Method. '''
        pass

    def do(self):
        '''
        Unit do someting. This is Abstract Method.
        Whenever the turn comes, do() is executed.
        '''
        pass

    def eval_self(self):
        '''
        proceed unit's dead.
        '''
        if self.heath_point <= 0:
            # character_state = dead
            self.is_dead

        # 랭크 변화 이미지 변경


class Player(Unit):
    def __init__(self, ct):
        self.name = ''
        self.set_name()
        super().__init__(ct)

        print(f'Player {self.name} is here')

    def set_name(self):
        '''
        set player name from user input.
        '''

        name = input('What is this character\'s new name')
        self.name = name

    def choose_target(self):
        pass

    def do(self):
        # 메뉴 선택 만들기
        selected = input()

        if selected == 'a':
            target = self.choose_target()
            self.attack(target)
        else:
            self.heal()

        self.eval_self()
        '''
        공격할지 않할지 고르고 해당 동작을 실행한다.
        :return:
        '''


class AI(Unit):
    def __init__(self, ct):
        self.name = 'AI' + str(randint(10, 99))
        self.manager = None
        super().__init__(ct)


        print(f'AI {self.name} is here')


    def do(self, state):
        pass

    def choose_target(self):
        '''choose the lowest health point from the user's characters'''
        minHealth = 100
        for health in playerHealth:  # playerHealth is a list for the player's characters' health
            if minHealth > health:
                minHealth = health




