# Exercise 9-13: Dice
#
# Make a class called Die that can have an even number of sides. Write a
# method called roll_die() that use the randint() to simulate the roll of a
# die.

from random import randint


class Die:
    """This class simulates the roll of a die where the even number of sides
    can be defined."""
    def __init__(self, sides=6):
        if sides % 2:
            print("Please use an even number of sides!")
            self.sides = 0
        else:
            self.sides = sides

    def roll_die(self, times):
        """This method 'rolls' the die x number of times and prints the
        output to the screen."""
        print(f"Rolled {times} times with a die having {self.sides} sides:")
        for x in range(1, times + 1):
            if x == times:
                print(f"{randint(1, self.sides)}")
            else:
                print(f"{randint(1, self.sides)}, ", end="")
        print("")


die6 = Die()
die6.roll_die(10)

die10 = Die(10)
die10.roll_die(10)

die20 = Die(20)
die20.roll_die(10)
