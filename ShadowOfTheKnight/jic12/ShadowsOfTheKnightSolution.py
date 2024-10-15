# # Shadows of the Knight Solution
#
#
# ## 1. Problem description
#
# This document describes a solution to a coding challenge on
# [Codingame.com](Codingame.com). The challenge is called
# [Shadows of the Knight Coding Challenge](https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1).
# The backstory of the challenge is that _Batman_ is looking for a **Bomb** in a
# building. He is able to determine the direction of the **Bomb** from his
# current location. _Batman_ has a limited number of jumps that he can make
# before the **Bomb** detonates. To solve the challenge, _Batman_ must implement
# a binary search algorithm to find the **Bomb** in time.

# ## 2. Reference Information
# The search algorithm starts with a full search space and reduces it by half in each iteration. _Batman_ starts in the middle of the current space, and the boundaries are updated based on the direction of the **Bomb**. This approach guarantees the search converges quickly.
#
# ### Images
#
# 1. Map setup: In the following example, _Batman_ starts in the lower left hand
# corner (0,0). The map is 50 units wide and 50 units tall.
# 2. First Jump: _Batman_ discovers that the **Bomb** is to his upper
# right so he jumps halfway between the vertical boundaries and halfway between
# the horizontal boundaries. Then he detects that the **Bomb** is to his lower
# left. This means that the **Bomb** cannot be above him or to the right of him
# so the right and top boundaries move in.
# 3. Second Jump: _Batman_ discovers that the **Bomb** is to his
# lower left so he jumps halfway between the vertical boundaries and halfway
# between the horizontal boundaries. Then he detects that the **Bomb** is to his
# upper right again. This means that the **Bomb** cannot be to the left or
# bellow his current location. Now the left and bottom boundaries move in.

# <img src="batmanStartPosition.png" style="width:375px;height:250px;">
# <img src="batmanFirstJump.png" style="width:375px;height:250px;">
# <img src="batmanSecondJump.png" style="width:375px;height:250px;">

# ## 3. Basic Binary Search Algorithm Discussion
# A basic [Binary Search Algorithm](https://www.geeksforgeeks.org/binary-search/) is
# able to efficiently find value in a sorted list. To do this, the algorithm
# tracks an upper and lower bound to subdivide the list until only one element remains. With each iteration through the loop,
# the algorithm determines whether the value that it is looking for is to the
# left or right of its current location. If the value is to the left of its
# current location, then the algorithm moves the upper bound to the current
# location -1. If the value is to the right of its current location, then the
# algorithm moves the lower bound to the current location +1. After the bounds
# have been adjusted, the current location is moved to halfway between the
# bounds. Binary search reduces the search space by half with each step, leading to logarithmic time complexity: O(log n) which almost always performs faster on an already sorted list.

# ### Generic Binary Search Algorithm
def binarySearch(list_, low, high, x):
    # params:
    # - list_: a list of sorted elements
    # - low: an integer representing the lowerbound
    # - high: an integer representing the upperbound
    # - x: the element being searched for
    # - return: the index of the element being searched for, or -1 in case the element is not found
    while low <= high:
        # Compute the index between the low and high\
        # Ex:
        # &nbsp;&nbsp;&nbsp;&nbsp;low, high = 5, 9\
        # &nbsp;&nbsp;&nbsp;&nbsp;mid = 5 + (9 - 5)//2 is 7
        mid = low + (high - low) // 2
        if list_[mid] == x:
            return mid
        elif list_[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ## 4. Solution
#
# ### Discussion
#
# The following algorithm differs from the basic binary search because it must
# keep up with upper and lower bounds for both the X and Y axes. As this
# algorithm runs, it simultaneously runs a binary search on both the X and Y
# axes. The advantage of this is that when the boundaries are moved, the
# algorithm does not need to consider values outside the boundary.

# ### Code

import sys
import math

# Variable descriptions:
# - mapWidth: width of the game grid
# - mapHeight: height of the game grid
# - jumpsUntilDetonation: how many jumps _Batman_ has to find the **Bomb**.
# - currentX, currentY: _Batman's_ current location on the map
# - farLeftBound, farRightBound: boundaries for the binary search across the x-axis
# - farBottomBound, farTopBound: boundaries for the binary search across the y-axis
# - bomb_dir: detected direction of the **Bomb** for each jump
mapWidth, mapHeight = [int(i) for i in input().split()]
jumpsUntilDetonation = int(input())
currentX, currentY = [int(i) for i in input().split()]
leftBound, rightBound = 0, mapWidth
bottomBound, topBound = mapHeight, 0

# With each iteration through the while loop, _Batman_ is given the direction of the **Bomb** in relation to his current location. Directions are provided as (U, UR, R, DR, D, DL, L, or UL).
# - D means down
# - U means up
# - R means right
# - L means left
# These can also be combined, meaning DL would represent down and left

while True:
    bomb_dir = input()
    print(bomb_dir, file=sys.stderr, flush=True)

    if "R" in bomb_dir:
        leftBound = currentX+1
    elif "L" in bomb_dir:
        rightBound = currentX-1

    if "D" in bomb_dir:
        topBound = currentY+1
    elif "U" in bomb_dir:
        bottomBound = currentY-1

    # _Batman_ now jumps to the halway point between the horizontal bounds and the halfway point between the vertical bounds.
    currentX = leftBound + (rightBound - leftBound) // 2
    currentY = bottomBound + (topBound - bottomBound) // 2

    print(currentX, currentY)