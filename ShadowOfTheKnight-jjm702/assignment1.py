import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

xmin, xmax, ymin, ymax = 0, w - 1, 0, h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from Batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if 'U' in bomb_dir:
        ymax = y0 - 1  # Narrow the vertical search range upwards
    if 'D' in bomb_dir:
        ymin = y0 + 1  # Narrow the vertical search range downwards
    if 'L' in bomb_dir:
        xmax = x0 - 1  # Narrow the horizontal search range to the left
    if 'R' in bomb_dir:
        xmin = x0 + 1  # Narrow the horizontal search range to the right
    
    # Update Batman's position to the middle of the new search area
    x0 = (xmin + xmax) // 2
    y0 = (ymin + ymax) // 2
    
    # Print the location of the next window Batman should jump to
    print(x0, y0)
