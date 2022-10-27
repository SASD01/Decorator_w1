from abc import abstractmethod
from abc import ABCMeta

class ICharacter(metaclass=ABCMeta):

    @abstractmethod
    def getDamage(self) -> int:
        pass