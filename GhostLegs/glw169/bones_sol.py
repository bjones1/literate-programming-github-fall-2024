import sys
import math
# # bones_sol.py - The solution to the *Ghost Legs* problem
#
# Here is a
# <a href="https://www.codingame.com/training/easy/ghost-legs" target="_blank" rel="noopener">link</a>
# to the Codingames exercise for this problem.
#
# ## The game & its input
#
# ![Ghost Legs Example Board](image001.png)
#
# Above is an annotated example image of the type of input the program expects.
# The goal of the game is to
#
# map all of the top labels to their corresponding bottom label by tracing a
# path along the "bones."
#
# When a trace encounters a bridge on its way down, it must move to the
# connected bone and continue downward.
#
# See the above image for completed example traces.
#
# ### Implementation
#
# #### Collecting & prepping input
#
# The first line of input is a width-height pairing for the dimensions of the
# game board to soon follow. Next is the row of bone labels which are the start
# of all the traces in the game. Afterwards, the ASCI art game board will be
# provided in lines of text. It is useful to note that bones and labels are
# spaced three characters across. *Bridges*, denoted by two hyphens, signify
# that the trace on that bone should move to the connected bone.
#
# Get and store the input dimension of the game and the line of labels
w, h = [int(i) for i in input().split()]
starting_line = input()
# Calculate the string index for each top label to relate it to a bone in the
# ASCI art input
# 
# Identify all labels and their respective string index
# Store each non-space character & its string index as a list pair in a list of labels
start_points = [[starting_line[i], i] for i in range(len(starting_line)) if starting_line[i] != ' ']
# #### **Parsing game board**
#
# Since the board is given line by line in the form of ASCI art, one must think
# about string indexing when probing the input line. In most languages accessing
# an index out of bounds for the string will result in an error. This is
# relevant when checking for bridges on the outer-most bones as no _bridges_
# will exist outside the board & thus out of bounds. Furthermore, checking the
# first bone's (index 0) left bridge (-1 offset) will index the string at -1,
# looping to the last character of a string in Python. While that character is
# guaranteed to be a bone and not a bridge it's better to handle this edge case.
#
# The idea used below is to explore any surrounding bridges for each bone and,
# while keeping track of which bone each top label is currently on, traverse
# them.
#
# **NOTE**: movements between bones are +/- 3 characters in the string
# Do not re-parse label lines (2 lines in total)
for i in range(h-2):
    line = input()
    moved = []
    # Iterate through each bone in the current line
    for idx in range(0, len(line)+1, 3):
        # The idea is to check each bone in the input line and, if a bridge is
        # next to it, have the trace for the label move to the connected bone.
        #
        # Rightmost bone edge-case: the rightmost bone cannot move further right
        if idx < len(line)-1:
            # Is there a branch to the right?
            if line[idx+1] == '-':
                for bone in start_points:
                    # Any bone trace here and not moved this loop?
                    if bone[1] == idx and bone[0] not in moved:
                        bone[1] += 3
                        moved.append(bone[0])
        # Leftmost bone edge-case: the leftmost bone cannot move further left
        if idx > 0:
            # Is there a branch to the left?
            if line[idx-1] == '-':
                for bone in start_points:
                    # Any bone trace here and not moved this loop?
                    if bone[1] == idx and bone[0] not in moved:
                        bone[1] -= 3
                        moved.append(bone[0])
ending_line = input()
# Now that each top label has traversed the bones to the bottom, they need to be
# mapped to the correct bottom label in order to produce the correct pairings as
# output. First, the bottom labels are extracted from the last input string. We
# then loop through the starting labels/points and, given their accompanying
# ending string index, we sample the end list of bottom labels with the integer
# division of the string index by 3, the distance between bones in the input.
# Finally, for each starting label, we output the start-end pair.
# 
# Calculate a string index for each label (1 + the integer division of the line width by 3)
end_points = [ending_line[i*3] for i in range(w//3+1)]
i = 0
while i < len(start_points):
    point = start_points[i]
    # Convert string index to bottom label index
    # The integer division by 3 of the string index gets the label index
    start_points[i] = [point[0], end_points[point[1]//3]]
    # Print out that label's output
    print(start_points[i][0] + start_points[i][1])
    i = i+1