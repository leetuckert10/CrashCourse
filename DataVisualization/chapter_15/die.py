# die.py
from random import randint
from typing import List


class Die:
    """This class models rolling a die with x number of sides."""

    # Keep up with the instances of die we have created.
    instances: List["Die"] = []

    def __init__(self, num_sides: int = 6):
        """Assume a 6-sided die."""
        self.num_sides = num_sides
        Die.instances.append(self)

    def roll(self) -> int:
        """Return an 'random' value between 1 and the number of sides."""
        return randint(1, self.num_sides)
