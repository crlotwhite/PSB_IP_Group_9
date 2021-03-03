from enum import Enum


class CharacterTypes(Enum):
    warrior = 'warrior'
    tanker = 'tanker'

    @classmethod
    def make_list(cls):
        result = []

        # __member__ is dictionary type.
        for k, _ in cls.__members__.items():
            result.append(k)

        return result
