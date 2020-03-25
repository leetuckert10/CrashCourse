# dice_visual.py
# This version and the Die class have enhancements beyond what was laid out
# in Crash Course such that rolling multiple dice is made much easier. You
# only change the number of dice in one place.

from typing import List, Dict
from plotly.graph_objects import Bar, Layout    # type: ignore
from plotly import offline                      # type: ignore

from die import Die


# Create multi-sided dice.
num_dice: int = 6
num_sides: int = 6
num_rolls: int = 500_000
max_result: int = 0
for x in range(1, num_dice + 1):
    die = Die(num_sides)
    max_result = max_result + die.num_sides

# We roll the number dice 1,000 times and then we store the sum of the dice
# in a list.
results: List[int] = []
result: int = 0
for roll in range(1, num_rolls + 1):
    for die in Die.instances:
        result = result + die.roll()
    results.append(result)
    result = 0

# Analyze the results. Bar() needs a list of values in the call to it.
frequencies: List[int] = []
for value in range(num_dice, max_result + 1):
    frequencies.append(results.count(value))

# The sum of all sides is the maximum number that can be returned and the
# minimum number that can only be 1 times the number of dice.
# Convert the range of sides to a list for the call to Bar().
x_values: List[int] = list(range(num_dice, max_result + 1))
data: List[Bar] = [Bar(x=x_values, y=frequencies)]

# The 'dtick' dictionary argument tells Plotly to label every tick mark.
x_axis_config: Dict = {'title': 'Result', 'dtick': 1}
y_axis_config: Dict = {'title': 'Frequency of Result'}
title_str: str = f"Results of rolling {num_dice} D{num_sides} {num_rolls} " \
                 f"times."
my_layout: Layout = Layout(title=title_str, xaxis=x_axis_config,
                           yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
