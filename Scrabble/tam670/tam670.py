import sys, math
# # Max Scrabble Score Calculator (scrabble.py)
#
# ## Problem and Approach
#
# This challenge asked us to find the valid word in the given dictionary with
# the highest possible scrabble score from the set of 7 tiles given to us. The
# dictionary is a list of strings given to us by the game. The score is
# calculated by tallying up the point values of each letter in the word (see
# corresponding chart below).  My approach is to compare each word in the given
# dictionary to my tiles, letter by letter. This will ensure that I can find all
# of the valid words that I can make with the letters.


# | Points | Letters                      |
# | ------ | ---------------------------- |
# | 10     | q, z                         |
# | 8      | j, x                         |
# | 5      | k                            |
# | 4      | f, h, v, w, y                |
# | 3      | b, c, m, p                   |
# | 2      | d, g                         |
# | 1      | a, e, i, o, u, l, n, s, t, r |
#
# From this, the word with the maximum score can be calculated.
#
# ## Inputs
#
# Below are the inputs from the game. These are needed to get the solution. This
# code was given by the site.The variable _n_ is the number of words in the
# dictionary. This loop gathers the dictionary of words and puts them in a list.
# This input is the string of letter that you have (7 letters). This loop
# gathers the dictionary of words and puts them in a list

n = int(input()) 
dictionary = []
for i in range(n):
    w = input()
    dictionary.append(w)
letters = input()

# ## Main Code
#
# ### Initialize Variables
#
# _max_ will store the max number of points possible. _hiword_ will store the
# word with that score
max = 0
hiword = ''

# ### Find Maximum Word
#
# We will loop through all the words in the dictionary list. The below syntax of
# **for x in list** works like this. It sets x to the 0th index of the list. At
# the end of the for loop, it then sets _x_ to the 1st index and so on. The loop
# will execute all elements in the list. For my program, **for word in
# dictionary** will loop through the whole _dictionary_ list, setting each to
# _word_.

for word in dictionary:

    # We will use the variable _templetters_, in case we need to make any
    # temporary changes to the letter set . The variable _buildword_ will store
    # the word we are building with the letter set
  
    templetters = letters
    buildword = ''

    # #### Find Possible Word
    #
    # To check if a word in the dictionary is possible with my tiles, I go
    # through each letter of the word. If the letter is correct, I "remove" it
    # from my tiles (this is why I created a temporary letter set). I then add
    # it to the word I am trying to build. Once we get to a letter that is not
    # in our tile set, we can **continue** to the next word in the dictionary
    
    for i in range(len(word)):
        if word[i] in templetters:
            templetters = templetters.replace(word[i], '', 1)
            buildword += word[i]
        else:
            continue
        if word == buildword:
            score = 0

            # #### Calculate Score
            #
            # Letters are awarded points based on the values in the table above.
            
            for letter in buildword:
                if letter in ['q', 'z']:
                    score += 10
                elif letter in ['j', 'x']:
                    score += 8
                elif letter in ['k']:
                    score += 5
                elif letter in ['f','h','v','w','y']:
                    score += 4
                elif letter in ['b','c','m','p']:
                    score +=3
                elif letter in ['d','g']:
                    score +=2
                else:
                    score += 1

            # #### Replace High Score
            #
            # If this score is higher than the current high score, we can
            # replace.
            
            if score > max:
                max = score
                hiword = word

# ### Output
#
# Now we output the word that gives us the highest possible score from our
# letter set.

print(hiword)
