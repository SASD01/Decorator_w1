from abc import abstractmethod
from abc import ABCMeta
from ICharacter import ICharacter


class CharacterDecorator(ICharacter, metaclass=ABCMeta):
    character: ICharacter

    def __init__(self, character: ICharacter) -> None:
        self.character = character

    def getDamage(self) -> int:
        return self.character.getDamage()