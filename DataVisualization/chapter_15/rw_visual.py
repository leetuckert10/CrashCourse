# rw_visual.py
# This is the final version of rw_visual.py which includes all the Exercises
# 15-1 through 15-5.

import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Make a random walk.
    rw: RandomWalk = RandomWalk(num_points=5_000, distance='high')
    rw.fill_walk()

    # Now plot the points in the walk.
    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_title("'Random' Walk", fontsize=24)

    # Accent starting and ending points and use a color map to demonstrate the
    # path taken by random walk.
    point_numbers = range(rw.num_points)
#   ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.get_cmap(
#       'plasma'), edgecolors=None, s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.scatter(0, 0, c='green', edgecolors=None, s=75)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=75)

    # Don't display axis values.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running: str = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
