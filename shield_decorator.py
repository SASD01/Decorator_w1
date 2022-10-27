from character_decorator import CharacterDecorator


class ShieldDecorator(CharacterDecorator):
    
    def getDamage(self) -> int:
        return self.character.getDamage() - 50 if self.character.getDamage() - 50 > 0  else 0