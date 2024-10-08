# ### Power of Thor - Episode 1
#
# <span style="background-color: #fbeeb8;">Waa94 : Very clear title, I would
# also suggest to write this title with Heading 1</span>
#
# **Link to the problem :
# [CodinGame Power of Thor](https://www.codingame.com/training/easy/power-of-thor-episode-1)**
# <span style="background-color: #fbeeb8;">Waa94 : Good idea to add the link, I
# would also sugest to make "<em>Link to the problem</em>" in italic instead of
# bold font</span>
#
# ### **Problem Overview:**
#
# <span style="background-color: #fbeeb8;">Waa94 : I think you tried to make an
# heading with the right command but you add bold also</span>
#
# <span class="hljs-comment">In this puzzle, Thor needs to move toward the
# light's position. Each turn, you need to print the direction</span>
# <span class="hljs-comment">in which Thor should move: North (N), South (S),
# East (E), or West (W). Thor's initial position is
# defined</span>      <span class="hljs-comment">&nbsp;by
# <code>initial_tx</code> and <code>initial_ty</code>, while the light is
# located at <code>light_x</code> and <code>light_y</code>.</span>
#
# ### **Overview of the algorithm:**
#
# ![Sketch](thor.jpg)

# Read input from standard input
input_data = sys.stdin.readline().split()
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input_data]
import sys
import math 
# **Game loop** <span style="background-color: #fbeeb8;">Waa94 : it's a good
# title, may be skip a line to appreciate it better here</span> The loop
# calculates and prints the direction Thor must go on each turn.
while True:
    remaining_turns = int(input())  
    # **Determine Direction** <span style="background-color: #fbeeb8;">Waa94 may
    # be skip a line here to make it easier to read </span> Thor moves East or
    # West depending on the position of `light_x` relative to `initial_tx`.
    if light_x > initial_tx:
    # Move East if the light is further right.
        direction_x = "E"  

@@ -40,43 +51,49 @@

    # Thor moves North or South depending on the position of `light_y` relative
    # to `initial_ty`.
    
    # <span style="background-color: #fbeeb8;">Waa94 : the algorithm is
    # efficent, I would also suggest to add title with heading before the
    # condition on X and Y to make a more visible separation</span>
    if light_y > initial_ty:
    # Move South if the light is below Thor.
        direction_y = "S"  
    elif light_y < initial_ty:
    # Move North if the light is above Thor.
        direction_y = "N"  
    else:
     # No movement in the Y direction if aligned.
        direction_y = "" 

    # **Update Thor's Position** <span style="background-color: #fbeeb8;">Waa94
    # : may be skip a line here to make it easier to read </span> Update Thor's
    # Y position if there is movement in the Y direction.
    if direction_y != "":
        if direction_y == "S":
        # Move South (increase Y).
            initial_ty += 1  
        else:
         # Move North (decrease Y).
            initial_ty -= 1 

    # Update Thor's X position if there is movement in the X direction.
    if direction_x != "":
        if direction_x == "E":
        # Move East (increase X).
            initial_tx += 1  
        else:
        # Move West (decrease X).
            initial_tx -= 1  

    # **Output Direction** Output the combined direction for Thor's movement
    # this turn.
    print(direction_y + direction_x)

# **Conclusion** <span style="background-color: #fbeeb8;">Waa94 : Very good
# Conclusion, I suggest to use heading here too</span>
#
# This program ensures Thor moves optimally towards the light using the shortest
# path. Thor stops when his position matches the light's coordinates or when he
# runs out of moves.