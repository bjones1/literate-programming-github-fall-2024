# # assignment1.py -- Python Solution for "Shadow of the Knight - Episode 1"

# ## **Objective**
# This Python program is designed to solve the puzzle
# [Shadow of the Knight - Episode 1](https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1)
# from Codingame. The objective of this puzzle is to guess the coordinates of a
# bomb in a 2D array by making guesses based on feedback provided in the form
# of directional hints.

# ## **Problem Statement**
# The goal of this puzzle is to **determine the location of a bomb within a
# rectangular grid**. You start with a guess and receive feedback on the
# direction of the bomb relative to your current position. You must adjust your
# guesses accordingly while **minimizing the number of attempts**.

# ### **Rules**
# The heat-signature device provides directions based on your current position
# and the general direction towards the bomb:
# - **U** (_Up_)
# - **UR** (_Up-Right_)
# - **R** (_Right_)
# - **DR** (_Down-Right_)
# - **D** (_Down_)
# - **DL** (_Down-Left_)
# - **L** (_Left_)
# - **UL** (_Up-Left_)

# Your mission is to **move Batman to the most likely position of the bomb in
# the fewest moves possible**. The building is represented as a grid where the
# top-left corner is at index (0,0).

# Below is an image depicting the basics of the problem with Batman on a random
# (x, y) and the bomb somewhere on the grid. The search interval is based on the
# direction given, which in this example would be 'UR':

# ![Example Grid](grid_plot.png)

# ## **Approach**
# Understanding the problem involves recognizing that the provided direction
# **reduces the possible search area**. The approach uses binary search
# principles to efficiently narrow down the potential locations of the bomb.

# - **Initial Setup:** Define the boundaries of the search area based on the
#   dimensions of the building.
# - **Direction Handling:** Update the search area boundaries according to the
#   given direction.
# - **Position Update:** Move Batman to the midpoint of the updated search area.
# - **Iteration:** Continue until the bomb's location is determined.

# Below is a block diagram illustrating the approach:

# ![Order of events](events.dot.svg)

# ## **Additional Content**

# - _What are intervals again?_
#   [Interval (mathematics)](https://en.wikipedia.org/wiki/Interval_(mathematics))
# - _Binary search basics:_
#   [GeeksforGeeks - Binary Search](https://www.geeksforgeeks.org/binary-search/)

# ## **Solution**

# ### **Imports**
import sys
import math

# ### **Initialization**

# #### w: width of the building, h: height of the building
w, h = [int(i) for i in input().split()]

# #### Maximum number of turns before game over.
n = int(input())  

# #### Starting coordinates for Batman.
x0, y0 = [int(i) for i in input().split()]

# #### Custom boundaries for search area
xmin, xmax, ymin, ymax = 0, w - 1, 0, h - 1

# ### **Main Game Loop**

while True:
    # #### Direction of the bombs from Batman's current location.
    bomb_dir = input()

    # #### Narrow the search range based on the direction
    if 'U' in bomb_dir:
        ymax = y0 - 1
    if 'D' in bomb_dir:
        ymin = y0 + 1
    if 'L' in bomb_dir:
        xmax = x0 - 1
    if 'R' in bomb_dir:
        xmin = x0 + 1

    # #### Update Batman's position to the middle of the new search area
    x0 = (xmin + xmax) // 2
    y0 = (ymin + ymax) // 2

    # #### Print the location of the next window Batman should jump to
    print(x0, y0)
