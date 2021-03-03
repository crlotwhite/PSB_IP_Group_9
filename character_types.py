from enum import Enum


class CharacterTypes(Enum):
    # Unit's character type
    warrior = 'warrior'
    tanker = 'tanker'

    @classmethod
    def make_list(cls):
        '''It combines the properties of an enum into a list.'''

        result = []

        # __member__ is dictionary type.
        for k, _ in cls.__members__.items():
            result.append(k)

        return result
