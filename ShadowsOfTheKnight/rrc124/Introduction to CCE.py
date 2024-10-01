import sys
import math 

# # Shadows of the Knight
# ## In this problem, Batman must find a bomb hidden in a building by using the least number of jumps.
# My approach uses _binary search_ to minimize the number of guesses.
# ---
# ![Diagram illustrating the binary search process](CCE_Image.png)
#
# The following was pre-coded by
# [Codingame](https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1)

# # Auto-generated code below aims at helping you parse the standard input
#
# according to the problem statement. w: width of the building. h: height of the
# building.
num_horiz_cells, num_vert_cells = [int(i) for i in input().split()] 
n = int(input())  # maximum number of turns before game over. 
x0, y0 = [int(i) for i in input().split()] 
# initialize the boundaries of the building Initialize the boundaries of the
# search space
#
# ## My Code Begins Here:
left_boundary, right_boundary = 0, num_horiz_cells - 1
top_boundary, bottom_boundary = 0, num_vert_cells - 1
# **The while loop is where Batman updates his position after getting directional hints.**
# **Within the loop, the game will provide hints about the bomb's location in relation to the
# location of Batman on the grid.** 
# **Based on the provided hints, Batman must adjust his area of search
# using _Binary Search_.**
# **This process will repeat until Batman finds every bomb location**
while True:
    bomb_dir = input()  

    # **The direction of the bomb from Batman's current location _(U, UR, R, DR,
    # D, DL, L or UL)_.**
    if 'U' in bomb_dir:
        bottom_boundary = y0 - 1
    elif 'D' in bomb_dir:
        top_boundary = y0 + 1
    if 'L' in bomb_dir:
        right_boundary = x0 - 1
    elif 'R' in bomb_dir:
        left_boundary = x0 + 1

    # This code updates the position of Batman to the middle of the new search
    # space.
    x0 = (left_boundary + right_boundary) // 2
    y0 = (top_boundary + bottom_boundary) // 2

    # Print the next position Batman should jump to
    print(f"{x0} {y0}")
# **This is a snapshot of the game. Here we see batman finding and disarming a
# bomb.** 
#
# ![Snapshot of Batman Finding Bombs](Game_Snapshot.png)
