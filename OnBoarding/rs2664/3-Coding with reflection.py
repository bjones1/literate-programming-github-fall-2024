# # [On Boarding Game Program](https://www.codingame.com/training)
#
# ## Problem-Solving Methodology
#
# ### **Comprehension of the Problem:**
#
# The task involves comparing the Euclidean distances between a reference point
# (representing our position) and two enemies, situated in a one-dimensional
# space. The objective is to determine which enemy is closest, as this
# represents the most immediate threat.
#
# ### Initial Thoughts:
#
# To clarify the problem, the scenario was conceptualized as occurring within a
# <span style="text-decoration: underline;">Euclidean space</span>, where two
# enemies are positioned at distinct points. The task is to ascertain which
# enemy is nearer by evaluating their respective distances from the reference
# point. A straightforward condition check was then considered, wherein the
# distances of the two enemies are compared, with
# <span style="text-decoration: underline;">the enemy having the shorter
# distance being identified as the immediate threat</span>.
      
# ### _<span style="text-decoration: underline;">Visualization and Planning <img src="C:\Users\HP\Downloads\Fall 2024\Literate Programing" alt="">:</span>_
#
# Prior to coding, a graphical representation of the problem.
# <img src="Drawing-1.jpg" alt="" width="625" height="715">
 
# ### *Components of the Program:*              
 # 1.  **Input**: The program takes the names and distances of two enemies as
 #     inputs.
 # 2.  **Comparison**: It compares the two distances.
 # 3.  **Output**: The program prints the name of the closest enemy.

import sys
import math

# #### **Function to determine the closest enemy**
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
