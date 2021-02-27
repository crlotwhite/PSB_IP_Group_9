from random import choice

from tkinter import PhotoImage

from unit import Player, AI
from character_types import CharacterTypes
from image_positions import *


class GameManager:
    class Slot:
        def __init__(self, c, h, r, n, u):
            self.character_position = c
            self.hp_position = h
            self.rank_position = r
            self.name_position = n
            self.unit = u
            self.character_image = PhotoImage(file='./resources/{}.png'.format(u.character_type))
            self.rank_image = PhotoImage(file='./resources/Rank{}.png'.format(u.level))

            from tkinter import StringVar
            self.hp_string_var = StringVar()
            self.name_string_var = StringVar()

        def update_level_image(self):
            self.rank_image = PhotoImage(file='./Rank{}.png'.format(self.unit.level))

    def __init__(self):
        self.unit_slot = []

        character_types_list = list(map(lambda x: x[1], CharacterTypes.choices()))
        is_user = True
        for c, h, r, n in zip(CHARACTER_POSITION_LIST, HP_POSITION_LIST, RANK_POSITION_LIST, NAME_POSITION_LIST):
            character_type = choice(character_types_list)
            if is_user:
                unit = Player(character_type)
            else:
                unit = AI(character_type)

            self.unit_slot.append(self.Slot(c, h, r, n, unit))
            is_user = not is_user
