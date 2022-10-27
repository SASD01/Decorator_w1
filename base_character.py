from ICharacter import ICharacter

class BaseCharacter(ICharacter):

    def getDamage(self) -> int:
        return 100
