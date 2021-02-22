from random import choice

from tkinter import PhotoImage

from unit import Player, AI
from character_types import CharacterTypes
from image_positions import *


class GameManager:
    class Slot:
        def __init__(self, c, h, r, u):
            self.character_position = c
            self.hp_position = h
            self.rank_position = r
            self.unit = u
            self.character_image = None #PhotoImage(file='./{}'.format(u.character_type))
            self.rank_image = None #PhotoImage(file='./rank_{}'.format(u.level))

        def update_level_image(self):
            self.rank_image = PhotoImage(file='./rank_{}'.format(self.unit.level))

    def __init__(self):
        self.unit_slot = []

        character_types_list = list(map(str, CharacterTypes))
        is_user = True
        for c, h, r in zip(CHARACTER_POSITION_LIST, HP_POSITION_LIST, Rank_POSTION_LIST):
            character_type = choice(character_types_list)
            if is_user:
                unit = Player(character_type)
            else:
                unit = AI(character_type)

            self.unit_slot.append(self.Slot(c, h, r, unit))
            is_user = not is_user
