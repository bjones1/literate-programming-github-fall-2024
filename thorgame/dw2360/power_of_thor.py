# # Power of Thor Game: [Codinggame.com](https://www.codingame.com/ide/puzzle/power-of-thor-episode-1)
# ## Imports

import sys
import math

# ## **Game Objective**
#

# <mark>JJM702: (Good use of headings and clear topic sentences.Is *approach* the appropriate heading? It seems this is a detailed explanation of the events of the game. The approach should be your approach to solving this probelm and what you will do. This seems to be under *Fixes* which is to me, unclear.)</mark>

# Use the compass directions to move Thor 1 cell in either direction to reach
# the light of power.
#
# You lose by Thor running out of energy or running off the map (40 x 18 grid).
#
# ## **Approach**
# ![Logic](logic.png)
#
# > The conditional statements begin with comparing Thor's initial XY position
# > to where the light of power's XY position is located.
#
# > The grid's coordinates begin at the top left corner with X = 0 & Y = 0.
#
# > This makes the bottom right corner have the coordinates: X = 39 & Y = 17.
#
# > If Thor's position is to the left of the light of power, then Thor must go
# > East hence his position should increase by 1 to reach the light of power.
#
# > Going West would decrease by one, and going North would decrease by 1 since
# > Thor's Y position would be greater than the light of power.
#
# > Going South would increase by one, and similar rules would apply for
# > directions: SE, SW, NE, NW
#
# > #### _Note_: Not all directions are provided since the test cases only required a minimum number of directions.
#
# ### **Variables**
#
# - _light_x_: the X position of the light of power
# - _light_y_: the Y position of the light of power
# - _initial_tx_: Thor's starting X position
# - _initial_ty_: Thor's starting Y position
#
# ### **Logic**
# ![Example](thorgame_example.png)
#
# ## **Solution**

# Variables
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# Game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print To debug: print("Debug messages...",
    # file=sys.stderr, flush=True)

# <mark>JJM702: (The logic in the following conditionals is somewhat confusing due to the use of a single `&` operator, which is a bitwise AND. In Python, use `and` for logical AND, or `&` for bitwise operations. Here, you likely meant to use `and`.)</mark>

    if initial_ty < light_y and initial_tx < light_x:
        initial_ty = initial_ty + 1
        initial_tx = initial_tx + 1
        print("SE")
# <mark>JJM702: (Comments above code explaining what the code does.)</mark>
    elif initial_ty < light_y and initial_tx > light_x:
        initial_ty = initial_ty + 1
        initial_tx = initial_tx - 1
        print("SW")

    elif initial_ty > light_y:
        initial_ty = initial_ty - 1
        print("N")

    elif initial_tx < light_x:
        initial_tx = initial_tx + 1
        print("E")

    elif initial_tx > light_x:
        initial_tx = initial_tx - 1
        print("W")
  
# <mark>JJM702: (Code reads well in editor. For codeChat you could consider using bold, italic, and underline to denote specific aspects clearly. Lack of visual aids hurts understanding.)</mark>
# <mark>JJM702: (Indentation and spacing in text could be improved. Grammatically it seems fine. Could use more custom description overall to explain your thoughts e.g. relay information about the game quickly and then introduce your problem solving approach and highlight key insights.)</mark>