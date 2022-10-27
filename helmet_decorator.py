from character_decorator import CharacterDecorator


class HelmetDecorator(CharacterDecorator):
    
    def getDamage(self) -> int:
        return self.character.getDamage() - 20 if self.character.getDamage() - 20 > 0  else 0