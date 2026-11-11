import random

class Dice:
    """Represent a dice that is rolled before turn"""

    def __init__(self, sides: int = 6) -> None:
        """Represent a dice with a given number of n-sides (default = 6)"""
        # Check if sides is atleast 2
        if sides <= 2:
            raise ValueError("Dice must have at least 2 sides.") 
        
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return the result"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allow the dice object to roll the dice created by d20 = Dice(sides=20) by calling d20()"""
        return self.roll()
