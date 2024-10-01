# <div align="center"><h1>The Descent Puzzle Solution</h1><h2>A Linear Search Approach to Identify the Tallest Mountain</h2><h3>Introduction to the CodeChat Editor</h3><p><strong>Written By:</strong> <em>Sean B. Corby</em></p><p><strong>Course:</strong> <em>ECE 4793/6793 - Literate Programming in Software Development</em></p></div>

# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span> Overall, I think that this was well done. Many of my comments are pretty minor. The document is thorough. I like the flowchart as a visual aid to go along with the code. The code reads well in the source code as well as in the literate programming document. The variable names were good. There were no grammer errors that I saw (not that I am the person to find those...). This document explains Linear Search well in addtion to describing why it is useful for this problem. 

# ## **Problem Breakdown**
#
# The goal of the puzzle is to identify the tallest mountain among eight and
# output its index. We are using a **linear search algorithm** to find the
# maximum height and its corresponding index. The solution is split into
# sections for initialization, looping through the input, checking conditions,
# and finally printing the result.
#
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>  
#
# - I think the topic sentence here is ambigious.
#   - Among eight what?
#   - To what is "its" referring?
# - To whom is "we" referring in the second sentence?
#
# ## **Linear Search Algorithm**
#
# The **linear search algorithm** is a simple method for finding a particular
# value (in this case, the maximum height) in a list of values (the mountain
# heights). The algorithm works by starting from the first element in the list
# and sequentially comparing each element to the current maximum value. If the
# element being examined is larger than the current maximum, it updates the
# maximum. The search continues until all elements have been checked.
#
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>   
#
# - I would say that "of values" in the first sentence is redundant.
# - You swap between using values and elements. I think that being more
#   consitent with terminology would make this more clear.
#
# **Why Linear Search?** Linear search is intuitive and straightforward, which
# makes it well-suited for small datasets like the eight mountains in this
# puzzle. Although more efficient algorithms such as binary search exist, they
# are unnecessary here because:
#
# 1.  The list of mountain heights is small, with only eight elements, making
#     the simplicity of linear search a good fit.
# 2.  Linear search works well with unordered data, as in this case where the
#     mountain heights are not pre-sorted.
# 3.  It has a time complexity of **O(n)**, meaning it performs a single pass
#     over all elements, which is efficient given the limited size of the input.
#
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>  
# - I do think that Linear Search is a good solution to this problem for the reasons that you mentioned.
# - Binary Search requires a sorted list. This makes Binary Search unnecessary
#   for this problem since once the list is sorted, the largest mountain would
#   be the last element in the list.
# - Another approach here could be to put the mountain values and index postions
#   in a dictionary and find the maximum item in the dictionary.
#
# ## **Flowchart Overview**
#
# The following flowchart visually outlines the steps taken to solve the puzzle.
# It breaks down the initialization of variables, the iteration through the list
# of mountains, the condition check for the tallest mountain, and the final
# output of the result.
#
# ![Flowchart showing the linear search algorithm steps: initializing variables, iterating through mountains, checking heights, and printing the index of the tallest mountain.](final_solution_flowchart.png)
#
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>  
#
# - Flowharts need different shapes for various portion of a program
#   [See this for more details](https://www.zenflowchart.com/flowchart-symbols)
# - It may be a convention that I am not aware of where a comment in a flowchart
#   goes to the right of the line, but I think that this could be made more
#   clear using the comment structure in the previous link as well.
#
# ### **Explanation**:
#
# - The flowchart begins by initializing the variables `max_height` and
#   `max_index`.
# - It then enters a loop that processes each mountain's height and compares it
#   with the current maximum.
# - The flowchart shows how the condition check updates the values if a taller
#   mountain is found.
# - Finally, the flowchart ends with the print statement that outputs the index
#   of the tallest mountain.
#
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>  
#
# - I think that pseudo code would be more useful here, but I am not sure if it
#   is needed.
#
# ## **Pre-Writing Reflections**
#
# Before writing the code, I recognized that the solution could be easily
# represented with a flowchart. Visualizing the process allowed me to break down
# the task into smaller, manageable sections. By dividing the problem into steps
# such as initialization, looping through inputs, checking conditions, and
# outputting the result, the coding phase became much more structured and
# simplified.
#
# I also anticipated potential issues with variable initialization, which could
# cause logic errors if not handled correctly. This led me to think through how
# to initialize the variables in a way that would ensure proper comparisons and
# updates within the loop.

# ## **Initialization**
#
# Before diving into the loop, we need to initialize two variables:
#
# 1.  **max_height**: This stores the maximum height encountered so far.
#     - Initialize it to -1, ensuring no mountain will have a smaller height.
# 2.  **max_index**: This tracks the index of the highest mountain.
#     - It starts at 0, and will be updated as we find higher mountains.

max_height = -1  # Initializing max_height to a value lower than any possible height.
max_index = 0    # Initializing max_index to 0 to indicate the first mountain.

# ## **Main Loop**
#
# The main loop will iterate over the heights of all eight mountains provided in
# the input. Each mountain’s height is processed one at a time using a `for`
# loop. Inside the loop:
#
# - We read the current mountain's height.
# - We compare this height to `max_height`. If the current mountain's height is
#   greater than `max_height`, we update both `max_height` and `max_index`.

while True:
    for i in range(8):
        # Read the height of the current mountain.
        mountain_h = int(input())  # Input the height of each mountain
        
        # ## **Condition Check**
        #
        # If the current mountain is taller than the stored maximum
        # (`max_height`), we update:
        #
        # - `max_height` to the current mountain's height.
        # - `max_index` to the index of this mountain.
        if mountain_h > max_height:
            max_height = mountain_h  # Updating the maximum height encountered so far.
            max_index = i            # Storing the index of the tallest mountain.
          
# #### <span style="background-color: #f1c40f;">JIC12:&nbsp;</span>  
#
# - I feel like mixing the literate programming blocks in with the code like
#   this makes the code less readable. Maybe my opinion on this will change with
#   practice. I think that literate programming is great and should be standard,
#   but using it on this level seems to get in the way of the code rather than
#   making the code more clear.
# - I think that the use of end of line comments are most useful at this level,
#   and that literate programming is most useful at the function level (or in
#   this case whole program) and above.
    # ## **Result Output**
    #
    # After evaluating all mountains, the index of the tallest mountain is
    # printed. This step happens after all comparisons are done for the current
    # round of input.
    print(max_index)  # Output the index of the tallest mountain to be shot at.

# ## **Post-Coding Reflection**
#
# During the coding process, several key insights emerged that helped streamline
# the logic and improve accuracy:
#
# - **Initialization Matters**: Setting `max_height` to `-1` ensured that any
#   real mountain height would be larger, making the logic flow smoother. This
#   avoided potential errors in comparisons.
# - **Efficient Looping**: Ensuring that every mountain was checked exactly once
#   prevented any missed comparisons, which could have led to inaccurate
#   results.
# - **Simplicity of Linear Search**: Using a linear search allowed for easy
#   identification and correction of any logical errors during testing.
#
# **Reflecting on the process**:
#
# - Visualizing the solution with a flowchart first made the coding process
#   smoother.
# - Breaking down the problem into steps—initialization, looping, condition
#   checking, and output—clarified the solution and reduced debugging time.

# The **linear search algorithm** was chosen because:
#
# - It is straightforward and easy to implement.
# - The number of elements is small (only 8 mountains), so a more complex
#   algorithm would not add significant value.
# - Linear search does not require the list to be sorted, which makes it ideal
#   for our input.

# **Insights gained during coding**: Initially, it was important to ensure that
# the variables were initialized correctly. I set `max_height` to -1, which made
# sure that any mountain height would be greater than the initial value. This
# approach helped streamline the logic inside the loop. Another important
# realization was ensuring that every mountain was checked exactly once, and the
# correct index was captured. The simplicity of the linear search allowed me to
# easily identify and resolve logical errors during the testing phase.
#
# **Reflecting on the process**, planning the solution with a flowchart first
# made the coding process smoother and more efficient. Breaking down the problem
# into smaller steps (initialization, looping, condition checking, and output)
# clarified the solution in advance, reducing the need for debugging during
# implementation.

# ## **References**
#
# - Knuth, Donald E. _Literate Programming_. Stanford University. Available at:
#   [Knuth Literate Programming](https://www-cs-faculty.stanford.edu/~knuth/lp.html)
# - Universal CTags Documentation. Available at:
#   [Universal CTags GitHub](https://github.com/universal-ctags/ctags)
