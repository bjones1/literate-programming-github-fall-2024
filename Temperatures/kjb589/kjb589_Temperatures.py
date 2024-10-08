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
# Try the puzzle yourself by clicking 
# [here](https://www.codingame.com/ide/puzzle/temperatures).
#
# **Inputs:**
#
# - _numTemps_, the number of temperatures to analyze
# - A string with _numTemps_ temperatures expressed as integers ranging -273 to 5526
#
# **Outputs**
#
# - Print the value of variable _closestTemp_, where _closestTemp_ is either:
#   - 0, if no temperatures are provided
#   - the temperature closest to 0, otherwise
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

numTemps = int(input())  # the number of temperatures to analyse

# Use **if-else** block to decide initial value of _closestTemp_. Initialize
# _closestTemp_ to 0 if _numTemps_ = 0 or to 5526 otherwise. 5526 will be the initial value
# because it is the largest input value possible with the given constraints.
if numTemps == 0:
    closestTemp = 0
else:
    closestTemp = 5526

for i in input().split():
    # _curr_: a temperature expressed as an integer ranging from -273 to 5526
    curr = int(i)
    
    # Compare absolute values to find value closest to zero. Store new input if
    # value is less than the current value of _closestTemp_.
    if (abs(curr) < abs(closestTemp)):
        closestTemp = curr
    
    # If _curr_ and _closestTemp_ are the same value, then store _curr_ if: _curr_
    # is greater than _closestTemp_ when compared directly. This ensures closest
    # stores the positive temperature, if two have the same absolute value.
    elif (abs(curr) == abs(closestTemp)):
        if (curr > closestTemp):
            closestTemp = curr

print(closestTemp)
