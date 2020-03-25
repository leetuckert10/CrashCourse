# die_visual.py

from typing import List, Dict
from plotly.graph_objects import Bar, Layout    # type: ignore
from plotly import offline                      # type: ignore

from die import Die


# Create a 6-sided die.
die: Die = Die()
results: List[int] = []

for roll in range(1, 1_000):
    result: int = die.roll()
    results.append(result)

# Analyze the results. Bar() needs a list of values in the call to it.
frequencies: List[int] = []
for value in range(1, die.num_sides + 1):
    frequency: int = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Convert the range of sides to a list for the call to Bar().
x_values: List[int] = list(range(1, die.num_sides + 1))
data: List[Bar] = [Bar(x=x_values, y=frequencies)]

x_axis_config: Dict = {'title': 'Result'}
y_axis_config: Dict = {'title': 'Frequency of Result'}
my_layout: Layout = Layout(title='Results of rolling on D6 1,000 times.',
                           xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
