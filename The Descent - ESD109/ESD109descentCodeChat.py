# # Ethan Davis ESD109 The Descent CodeChat Editor



# This is _The Descent_, a game that can be found on
# [Codingame](https://www.codingame.com/ide/puzzle/the-descent) and is
# classified as an easy puzzle to solve. At first look of this program, I
# thought it to be too simple, but as was reinforced int he class there is no
# such thing as simple when the human factor is involved and imaginations run
# wild.  The while loop represents the game. Each iteration represents a turn of
# the game where you are given inputs (the heights of the mountains) and where
# you have to print an output (the index of the mountain to fire on) The inputs
# you are given are automatically updated according to your last actions. There
# are many different test cases for this that need to be passed, 5 in fact. In
# order to pass each of these a culmination of the different types of loops and
# if statements that may be needed has to include all of these cases. Below is a
# simple diagram showing my process that I drew by hand when I first began to
# solve this problem.



# ![BlockDiagram / Flowchart](BlockDiagram.jpg)


# ## My solution code for the game is present below.
#
# For the code in the game, I followed a simplistic approach to solving the
# problem after becoming very frustrating with myself for not being able to
# overcome it within an hour. The reason that I did this was I went on a pure
# tangent trying to overcomplicate something that did not need to be
# complicated!
import sys
import math

# Since the code given and the instructions were given in a **while** loop, I
# will build off of what was given. There are multiple test cases, so for each
# test case the loop has to test for a baseline that the **while** loop can
# provide.
while True:
    # What is given is the _I_ in range of 8, however there is not a maximum set
    # for any of these values. _I_ is not given a minimum, or a maximum which
    # means that the ship will keep going until it dies and won't recognize its
    # coming doom.
    maximum_h = 0
    maximum_index = -1
    # From the for loop that was given to us, I then began to write and I went
    # through multiple variations that both worked and did not work. The most
    # notable are usign arrays and using another while loop that would break and
    # restart for each test case, however both cases were extremely complicated
    # and were not smooth. They had more room for error.
    for i in range(8):
        mountain_h = int(input())

        # Here, the code gives you an open option on what to do, while I could
        # do another **while** loop and jump through hoops, I will do a simple
        # _if_ loop with some conditions _If_ the mountain's current height is
        # more than the max height
        if mountain_h > maximum_h:
            # set the new max to be the current height.
            maximum_h = mountain_h
            # This new maximum index, taken from above in line 19 and given a
            # value in maximum_index, is now set to the _I_ given in the current
            # time
            maximum_index = i
    # Print this maximum index and it will then shoot the mountains in order as
    # it descends. This will show in the codingame website and game window as it
    # runs to show a visual representation of the ship blowing up mountains.
    print(maximum_index)

# ## Below is a small discussion on this game
#
# The game was a brainteaser while also being a very cohesive and have the
# ability to be simple. The code itself has a tendency to spark an overthinking
# process in the programmer tackling the problem. While multiple attempts could
# be made and it each different case can be correct, the simplicity of it and
# the ability for others to cohesively understand what the programmer did is the
# main focus for taking in the thought process.