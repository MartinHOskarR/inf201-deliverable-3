from dice import Dice

class Weapon:
    """Represents a weapon in the RPG"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon
        Args:
        name (str): The name of the weapon.
        damage_dice (Dice): The dice used to determine the damage dealt when the weapon is used.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice and return the result"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"