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

            :param c: (Tuple[int, int]) character_position
            :param h: (Tuple[int, int]) hp_position
            :param r: (Tuple[int, int]) rank_position
            :param n: (Tuple[int, int]) name_position
            :param u: (Union[Player, AI]) unit
            '''
            self.character_position = c
            self.hp_position = h
            self.rank_position = r
            self.name_position = n
            self.unit = u

            # Creates a PhotoImage object based on the specified file name.
            self.character_image = PhotoImage(file='./resources/{}.png'.format(u.character_type))
            self.rank_image = PhotoImage(file='./resources/Rank{}.png'.format(u.level))

            from tkinter import StringVar
            self.hp_string_var = StringVar()
            self.name_string_var = StringVar()

        def update_level_image(self):
            # update rank image
            self.rank_image = PhotoImage(file='./resources/Rank{}.png'.format(self.unit.level))

    def __init__(self):
        self.unit_slot = []
        self.player_slot = []
        self.ai_slot = []
        self.previous_target = None

        # Save it as a variable to avoid unnecessary method execution.
        character_types_list = CharacterTypes.make_list()

        # It is used to select the player and the AI in order.
        is_user = True

        # Multiple lists of values are stored in a specified order and processed at once.
        # This is the data needed to create an object.
        for c, h, r, n in zip(CHARACTER_POSITION_LIST, HP_POSITION_LIST, RANK_POSITION_LIST, NAME_POSITION_LIST):
            # Select a class randomly.
            character_type = choice(character_types_list)

            if is_user:
                unit = Player(character_type)
                self.player_slot.append(unit)
            else:
                unit = AI(character_type)
                self.ai_slot.append(unit)

            self.unit_slot.append(self.Slot(c, h, r, n, unit))
            is_user = not is_user

    def is_player_win(self):
        # True if the list of non-dead players is empty.
        return not any(filter(lambda unit: not unit.is_dead, self.ai_slot))

    def is_ai_win(self):
        # True if the list of non-dead AIs is empty.
        return not any(filter(lambda unit: not unit.is_dead, self.player_slot))
