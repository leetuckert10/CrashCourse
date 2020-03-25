# random_walk.py: This source file contains stuff.

from random import choice
from typing import List


class RandomWalk:
    """A class to generate 'random' walks."""

    def __init__(self,
                 num_points: int = 5000,
                 distance: str = 'medium') -> None:
        """Initialize class attributes for a 'random' walk."""
        self.num_points = num_points
        self.distance = distance
        self.x_values: List[int] = [0]
        self.y_values: List[int] = [0]

    def fill_walk(self) -> None:
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            x_step: int = self.get_step()
            y_step: int = self.get_step()

            # Reject movements that go nowhere4.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position and append the x and y values of the
            # new step.
            x: int = self.x_values[-1] + x_step
            y: int = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self) -> int:
        """This method determines the step value by multiplying the direction
        by the distance both values randomly selected."""

        # Decide which direction to go and how far to go in that
        # direction.  -1 is left and 1 is right.
        direction: int
        distance: int

        direction = choice([1, -1])

        if self.distance == 'low':
            distance = choice([0, 1, 2, 3])
        elif self.distance == 'high':
            distance = choice([0, 1, 2, 3, 4, 5, 6, 8])
        else:
            distance = choice([0, 1, 2, 3, 4, 5])  # default value

        step: int = direction * distance
        return step
