from Imbatibility_decorator import ImbatibilityDecorator
from base_character import BaseCharacter
from helmet_decorator import HelmetDecorator
from shield_decorator import ShieldDecorator


def main(): 
    # Base Character
    character = BaseCharacter()
    causedDamage = character.getDamage()
    print("Damage Base -> " + str(causedDamage))

    # Character With Helmet
    character = BaseCharacter()
    character = HelmetDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Helmet -> " + str(causedDamage))

    # Character With Shield
    character = BaseCharacter()
    character = ShieldDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Shield -> " + str(causedDamage))

    # Character With Imbatibility
    character = BaseCharacter()
    character = ImbatibilityDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Imbatibility -> " + str(causedDamage))

    #Character With Helmet and Shield
    character = BaseCharacter()
    character = HelmetDecorator(character)
    character = ShieldDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Helmet and Shield -> " + str(causedDamage))

    #Character With Shield and Helmet
    character = BaseCharacter()
    character = ShieldDecorator(character)
    character = HelmetDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Shield and Helmet -> " + str(causedDamage))    

    #Character With Helmet and Imbatibility
    character = BaseCharacter()
    character = ImbatibilityDecorator(character)
    character = ShieldDecorator(character)
    causedDamage = character.getDamage()
    print("Damage with Shield and Imbatibility -> " + str(causedDamage))

if __name__ == '__main__':
    main()