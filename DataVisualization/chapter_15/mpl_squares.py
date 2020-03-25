# mpl_squares.py

import matplotlib.pyplot as plt     # type: ignore
from typing import List             # type: ignore


squares: List = [1, 4, 9, 16, 25]
input_values: List = [1, 2, 3, 4, 5]
y_values: List = [1, 4, 9, 16, 25]
x_values: List = [1, 2, 3, 4, 5]

# Set the plot style.
plt.style.use("bmh")

fig, ax = plt.subplots()
# Emphasize certain points.
ax.scatter(x_values, y_values, s=100)
ax.plot(input_values, squares, linewidth=3)

# Setting labels and font sizes
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()