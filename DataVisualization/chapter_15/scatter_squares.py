# scatter_squares.py

import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Set the plot style.
plt.style.use("bmh")

fig, ax = plt.subplots()

# Emphasize certain points.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.get_cmap(
    'plasma'), s=10)

# Setting labels and font sizes
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()
