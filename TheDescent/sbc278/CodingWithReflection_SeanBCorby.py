import sys
import math

# game loop
while True:
    max_height = -1
    max_index = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > max_height:
            max_height = mountain_h
            max_index = i

    print(max_index)  # The index of the mountain to fire on.
