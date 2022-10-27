from character_decorator import CharacterDecorator


class ImbatibilityDecorator(CharacterDecorator):
    
    def getDamage(self) -> int:
        return self.character.getDamage() * 0