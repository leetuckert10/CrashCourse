# Exercise 15-1: Plot the first five cubic numbers and then plot the first
# 5000 cubic numbers.

import matplotlib.pyplot as plt         # type: ignore
from typing import List

upper_bound: int = 5001
input_values: range = range(1, upper_bound)
cubes: List[int] = [x**3 for x in range(1, upper_bound)]

# Set the plot style.
plt.style.use("bmh")

fig, ax = plt.subplots()
#ax.plot(input_values, cubes, linewidth=1, c='blue')

# Emphasize certain points.
ax.scatter(input_values, cubes, c=input_values, cmap=plt.cm.get_cmap(
    'plasma'), s=10)

# Setting labels and font sizes
ax.set_title("Cubed Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.scatter(input_values, cubes, s=2)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
