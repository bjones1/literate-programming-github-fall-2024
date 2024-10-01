# # [On Boarding Game Program](https://www.codingame.com/training)
#
# ##    *Problem-Solving Methodology*
#
# <span style="background-color: #f1c40f;">MBS</span>: Consider removing the indent beside "Problem-Solving Methodology" above
#
# ### <span style="text-decoration: underline;"><em><strong>Comprehension of the Problem:</strong></em></span>
# The task involves comparing the Euclidean distances
# between a reference point (representing our position)  and two enemies,
# situated in a one-dimensional space. The objective is to determine which enemy is closest, 
# as this represents the most immediate threat.
# ###       <span style="text-decoration: underline;"><em>Initial Thoughts:</em></span>
#
# <span style="background-color: #f1c40f;">MBS</span>: Consider removing the indent beside "Initial Thoughts:" above
#
# To clarify the problem, the scenario was conceptualized as occurring within a Euclidean space,
# where two enemies are positioned at distinct points. The task is to ascertain which enemy is 
# nearer by evaluating their respective distances from the reference point.
# A straightforward condition check was then considered, wherein the distances of the two enemies 
# are compared, with the enemy having the shorter distance being identified as the immediate threat.
      
# Prior to coding, a graphical representation of the problem.
#
# <span style="background-color: #f1c40f;">MBS</span>: moving the line above under "visualization and planning" will make it more clear you are referring to the image.
#
# ### _<span style="text-decoration: underline;">Visualization and Planning <img src="C:\Users\HP\Downloads\Fall 2024\Literate Programing" alt="">:</span>_

# <img src="Drawing-2.jpg" alt="" width="625" height="715">
 
# ### <span style="text-decoration: underline;"><em>Components of the Program:&nbsp;</em></span>       
 # 1. **Input**: The program takes the names and distances of  two enemies as inputs.
 # 2. **Comparison**: It compares the two distances.
 # 3. **Output**: The program prints the name of the closest enemy.

import sys
import math

# #### **Function to determine the closest enemy**

# <span style="background-color: #f1c40f;">MBS</span>: a short snippet here describing how this 'def' works as if the reader didnt know basic coding would be a nice addition.
def closest_enemy(enemy_1, dist_1, enemy_2, dist_2):

    if dist_1 < dist_2:

        return enemy_1  
    else:

        return enemy_2  
# **game loop**
while True:
    enemy_1 = input()  
    dist_1 = int(input())  
    enemy_2 = input()  
    dist_2 = int(input())  
  
# **Print the name of the closest enemy to shoot**
    print(closest_enemy(enemy_1, dist_1, enemy_2, dist_2))
