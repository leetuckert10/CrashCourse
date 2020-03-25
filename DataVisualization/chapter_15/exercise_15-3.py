# exercise_15-3.py

import matplotlib.pyplot as plt         # type: ignore

from random_walk import RandomWalk


# Make a random walk.
rw: RandomWalk = RandomWalk(50_000)
rw.fill_walk()

# Now plot the points in the walk.
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(15, 9))
ax.set_title("'Random' Walk", fontsize=24)

# Accent starting and ending points and use a color map to demonstrate the
# path taken by random walk.
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.get_cmap(
    'plasma'), edgecolors=None, s=1)
# ax.scatter(rw.x_values, rw.y_values, s=15)
ax.scatter(0, 0, c='green', edgecolors=None, s=75)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=75)

# Don't display axis values.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
