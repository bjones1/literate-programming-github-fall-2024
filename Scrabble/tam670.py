import sys, math
# # Max Scrabble Score Calculator (scrabble.py)
# ## Problem and Approach
# This challenge asked us to find the word with the highest possible scrabble score from the set of 7 tiles given to us. My approach is to compare each word in the given dictionary to my tiles, letter by letter. This will ensure that I can find all the valid words that I can make with letters. Then we can calucalte the scores based off the below table. 

# | Points | Letters |
# | --- | --- | 
# | 10  | q, z  |
# | 8 | j, x| 
# | 5 | k |
# | 4 | f, h, v, w, y |
# | 3 | b, c, m, p |
# | 2 | d, g |
# | 1 | a, e, i, o, u, l, n, s, t, r |

# From this, the word with the maximum score can be calculated.

# ## Inputs
# Below are the inputs from the game. These are needed to get the solution.
# This code was given by the site. 
#
# *n* is the number of words in the dictionary
n = int(input()) 
# This loop gathers the dictionary of words and puts them in a list
# 
# To see the full list of valid Scrabble words, visit [scrabble.merriam.com](https://scrabble.merriam.com/)
dictionary = []
for i in range(n):
    w = input()
    dictionary.append(w)
# This input is the string of letter that you have (7 letters)
letters = input()

# ## Main Code
# ### Initialize Variables
# *max* will store the max number of points possible. *hiword* will store the word with that score
max = 0
hiword = ''
# ### Find Maximum Word
# 
for word in dictionary:
    # We will use *templetters*, in case we need to make any temporary changes to the letter set
    templetters = letters
    # *buildword* will store the word we are building with the letter set
    buildword = ''
# #### Find Possible Word
    for i in range(len(word)):
        # To check if a word in the dictionary is possible with my tiles, I go thorugh each letter of the word. 
        if word[i] in templetters:
                # If the letter is correct, I "remove" it from my tiles (this is why I created a temporary letter set). i then add it to the word I am trying to build
            templetters = templetters.replace(word[i], '', 1)
            buildword += word[i]
        # Once we get to a letter that is not in our tile set, we can **continue** to the next word in the dictionary
        else:
            continue

        if word == buildword:
            score = 0
            #  
# #### Calculate Score
            for letter in buildword:
                # Letters are awarded points based on the values in the table above.

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
            # If this score is higher than the current high score, we can replace.
            if score > max:
                max = score
                hiword = word


# ### Output
# Now we output the word that gives us the highest possible from our letter set
print(hiword)
