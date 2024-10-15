# <div align="center">
# <h1>The Descent Puzzle Solution</h1>
# <h2>A Linear Search Approach to Identify the Tallest Mountain</h2>
# <h4>Introduction to the CodeChat Editor</h4>
# <h4>Written By: Sean B. Corby</h4>
# <h4>ECE 4793/6793 - Literate Programming in Software Development</h4>
# </div>
#
# ## **Problem Breakdown**
# The goal of the puzzle is to identify the tallest mountain among eight and
# output its index. We are using a **linear search algorithm** to find the
# maximum height and its corresponding index. The solution is split into
# sections for initialization, looping through the input, checking conditions,
# and finally printing the result.
#
# ## **Linear Search Algorithm**
# The **linear search algorithm** is a simple method for finding a particular
# value (in this case, the maximum height) in a list of values (the mountain
# heights). The algorithm works by starting from the first element in the list
# and sequentially comparing each element to the current maximum value. If the
# element being examined is larger than the current maximum, it updates the
# maximum. The search continues until all elements have been checked.
#
# **Why Linear Search?**
# 1. The list of mountain heights is small, with only eight elements, making
#    the simplicity of linear search a good fit.
# 2. Linear search works well with unordered data, as in this case where the
#    mountain heights are not pre-sorted.
# 3. It has a time complexity of **O(n)**, meaning it performs a single pass
#    over all elements, which is efficient given the limited size of the input.
#
# ## **Flowchart Overview**
# Below is a flowchart that visually represents the algorithm used to solve the
# problem:
#
# ![Flowchart of Solution](./final_solution_flowchart.png)
#
# ## **Initialization**
# Before diving into the loop, we need to initialize two variables:
#
# Code Block
max_height = -1  # Initializing max_height to a value lower than any possible height.
max_index = 0    # Initializing max_index to 0 to indicate the first mountain.
#
# ## **Main Loop**
# The main loop will iterate over the heights of all eight mountains provided in
# the input. Each mountain’s height is processed one at a time using a `for`
# loop.
#
# Code Block
while True:
    for i in range(8):
        # Read the height of the current mountain.
        mountain_h = int(input())  # Input the height of each mountain
#       
        # Condition Check
        if mountain_h > max_height:
            max_height = mountain_h  # Updating the maximum height encountered so far.
            max_index = i            # Storing the index of the tallest mountain.
#    
    # Result Output
    print(max_index)  # Output the index of the tallest mountain to be shot at.
#
# ## **Post-Coding Reflection**
# The code implements a simple **linear search algorithm** that finds the
# maximum value in a set of eight numbers (mountain heights). This algorithm
# runs in **O(n)** time complexity, meaning that the time it takes to complete
# the search grows linearly with the number of elements. Since we're only
# processing eight mountains, this is optimal for the task at hand.
#
# **Why Linear Search?**
# - It is straightforward and easy to implement.
# - The number of elements is small (only 8 mountains), so a more complex
#   algorithm would not add significant value.
# - Linear search does not require the list to be sorted, which makes it ideal
#   for our input.
#
# **Insights gained during coding**: 
# - Initially, it was important to ensure that the variables were initialized
#   correctly. I set `max_height` to -1, which made sure that any mountain
#   height would be greater than the initial value.
# - This approach helped streamline the logic inside the loop. Another
#   important realization was ensuring that every mountain was checked exactly
#   once, and the correct index was captured. The simplicity of the linear
#   search allowed me to easily identify and resolve logical errors during the
#   testing phase.
#
# **Reflecting on the process**: Planning the solution with a flowchart first
# made the coding process smoother and more efficient. Breaking down the problem
# into smaller steps (initialization, looping, condition checking, and output)
# clarified the solution in advance, reducing the need for debugging during
# implementation.
#
# ## **References**
# - Knuth, Donald E. _Literate Programming_. Stanford University. Available at:
#   [Knuth Literate Programming](https://www-cs-faculty.stanford.edu/~knuth/lp.html)
# - Universal CTags Documentation. Available at:
#   [Universal CTags GitHub](https://github.com/universal-ctags/ctags)