from random import choice

from tkinter import PhotoImage

from unit import Player, AI
from character_types import CharacterTypes
from image_positions import *


class GameManager:
    class Slot:
        def __init__(self, c, h, r, n, u):
            '''
            It stores the image and output coordinate information of each slot unit.

            :param c: character_position
            :param h: hp_position
            :param r: rank_position
            :param n: name_position
            :param u: unit
            '''
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
            self.rank_image = PhotoImage(file='./resources/Rank{}.png'.format(self.unit.level))

    def __init__(self):
        self.unit_slot = []

        # Returns the properties of an enumeration and the values of those properties as a tuple.
        # Among them, the contents of 'value' are made into a list and stored.
        character_types_list = list(map(lambda x: x[1], CharacterTypes.choices()))

        # It is used to select the player and the AI in order.
        is_user = True

        # Multiple lists of values are stored in a specified order and processed at once.
        # This is the data needed to create an object.
        for c, h, r, n in zip(CHARACTER_POSITION_LIST, HP_POSITION_LIST, RANK_POSITION_LIST, NAME_POSITION_LIST):
            # Select a class randomly.
            character_type = choice(character_types_list)

            if is_user:
                unit = Player(character_type)
            else:
                unit = AI(character_type)

            self.unit_slot.append(self.Slot(c, h, r, n, unit))
            is_user = not is_user
