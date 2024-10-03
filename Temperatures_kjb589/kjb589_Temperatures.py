# # Temperatures.py - Solution to the CodinGame puzzle
#
# ## Overview
#
# In this exercise, you have to analyze records of temperature to find the
# closest to zero. This puzzle exercises the use of conditions, lists, and for
# loops. Write a program that prints the temperature closest to 0 among input
# data. If two numbers are equally close to zero, positive integer has to be
# considered closest to zero (for instance, if the temperatures are -5 and 5,
# then display 5).
#
# <mark >BAB:</mark> Good explanation I can't find anything to critize here.
#
# Try the puzzle yourself by clicking 
# [here](https://www.codingame.com/ide/puzzle/temperatures).
#
# **Inputs:**
#
# - _N_, the number of temperatures to analyze
# - A string with _N_ temperatures expressed as integers ranging -273 to 5526
#
# **Outputs**
#
# - Print the value of variable _closest_, where _closest_ is either:
#   - 0, if no temperatures are provided
#   - the temperature closest to 0, otherwise
#
# <mark >BAB:</mark> Ok these variable names could use some work. I'd recommend _N_ be named _numTemps
# and _closest_ be named _closestTemp_ to make this easier to understand at a glance.
#
# ---
#
# ## The Strategy
#
# <img src="Temp_puzzle_notes.jpeg" alt="Puzzle Solution" width="600">
#
# ---
#
# ## The Implementation
import sys
import math

# Auto-generated code below aims at helping you parse the standard input
# according to the problem statement.

n = int(input())  # the number of temperatures to analyse

# Use **if-else** block to decide initial value of _closest_. Initialize
# _closest_ to 0 if _N_ = 0 or to 5526 otherwise. 5526 will be the initial value
# because it is the largest input value possible with the given constraints.
if n == 0:
    closest = 0
else:
    closest = 5526

for i in input().split():
    # _t_: a temperature expressed as an integer ranging from -273 to 5526
    curr = int(i)
    
    # Compare absolute values to find value closest to zero. Store new input if
    # value is less than the current value of _closest_.
    if (abs(curr) < abs(closest)):
        closest = curr
    
    # If _curr_ and _closest_ are the same value, then store _curr_ if: _curr_
    # is greater than _closest_ when compared directly. This ensures closest
    # stores the positive temperature, if two have the same absolute value.
    elif (abs(curr) == abs(closest)):
        if (curr > closest):
            closest = curr

print(closest)

# <mark >BAB:</mark> Looks good overall I but I noticed a number of grammar errors in your explanations.
# The grammar errors aren't major but they do make things akward to read.
# The solution is explained and it is easy to read. Great work!