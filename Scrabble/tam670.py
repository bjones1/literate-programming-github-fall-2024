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
# <span style="text-decoration: underline;">of</span> the valid words that I can
# make with <span style="text-decoration: underline;">the</span> letters.
#
# <span style="background-color: #fbeeb8;">dsr209:</span> I would say something
# at the end about how each letter correlates to a specific score then the score
# is totaled by adding each letters individual score together. I also added a
# few words to help with grammar and flow, I underlined them. After looking at
# the game rules on codingame, you need to include a better discription of the
# dictionary and how the user
#
# <span style="background-color: #2dc26b;">tam670</span> I added parts about the
# dictionary and how it is given. I also provided more context about how the
# score it calculated.

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
# <span style="background-color: #fbeeb8;">dsr209:</span> I really like the
# above table, it does a good job showing the reader the letters and their
# corresponding scores.\
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

# <span style="background-color: #fbeeb8;">dsr209:</span> I would add more of a
# description paragraph under the inputs heading. Describe in detail what each
# input is what it is for. I also think for the literate part of the
# programming, leaving the code seperate from the comments is ideal. It allows
# the reader to read what is going to happen and why and then see the code that
# does it.
#
# <span style="background-color: #2dc26b;">tam670</span> I have moved all the
# comments to above this set of code. I agree it does make the program more
# legible
#
# ## Main Code
#
# ### Initialize Variables
#
# _max_ will store the max number of points possible. _hiword_ will store the
# word with that score
max = 0
hiword = ''
# <span style="background-color: #fbeeb8;">dsr209:</span> I think the variables
# should be initialized at the beginning of the code but the naming is
# descriptive well done.
#
# <span style="background-color: #2dc26b;">tam670</span> I have decided to make
# no changes here, since this is the begining of the code.
#
# ### Find Maximum Word
#
# <span style="background-color: #fbeeb8;">dsr209:</span> How does this loop
# work? Where is "word" initialized? Is it just a part of the game?
#
# <span style="background-color: #2dc26b;">tam670</span> I am adding context to
# this below.
#
# We will loop through all the words in the dictionary list. The below syntax of
# <span style="text-decoration: underline;">for x in list</span> works like
# this. It sets x to the 0th index of the list. At the end of the for loop, it
# then sets x to the 1st index and so on. The loop will execute all elements in
# the list. For my program, <span style="text-decoration: underline;">for word
# in dictionary</span> will loop through the whole dictionary list, setting each
# to <span style="text-decoration: underline;">word</span>.

for word in dictionary:


    # We will use the variable _templetters_, in case we need to make any
    # temporary changes to the letter set . The variable _buildword_ will store
    # the word we are building with the letter set
  
    templetters = letters
    buildword = ''

    # #### Find Possible Word
    #
    # <span style="background-color: #fbeeb8;">dsr209:</span>  The comments
    # within the code make it hard to see what the code is doing in code chat. I
    # am also confused about how this code finds or builds a word. Also, "word"
    # is used again but declared nowhere, what is this variable.
    #
    # To check if a word in the dictionary is possible with my tiles, I go
    # through each letter of the word. If the letter is correct, I "remove" it
    # from my tiles (this is why I created a temporary letter set). I then add
    # it to the word I am trying to build. Once we get to a letter that is not
    # in our tile set, we can **continue** to the next word in the dictionary
    #
    # <span style="background-color: #fbeeb8;">dsr209:</span> Misspelling
    # highlighted in red. **Fixed**
    
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


# <span style="background-color: #fbeeb8;">dsr209:</span> The headings of your
# sections need to be indented to clearly convey which section of code they
# correlate to. Also create a paragraph discussing what each section does and
# the thought process behind it. Let the reader know and try to answer any
# questions you think they might ask. Then, once that is done, have the code
# that does it.
#
# ### Output
#
# Now we output the word that gives us the highest possible score from our
# letter set.
#
# <span style="background-color: #fbeeb8;">dsr208:</span> added a word to make
# it make more sense and a period at the end of the sentence.

print(hiword)

# ## <span style="background-color: #fbeeb8;">dsr209:</span> Overall 
#
# I think the writing is mostly clear and coherent but could use a bit of work.
# There is only one paragraph and that is the problem and approach paragraph.
# This paragraph conveys most of the information needed. There are several
# grammatical errors and at least one misspelling. The sentences were missing
# words or not worded very well. The code in codechat is difficult to read with
# the comments and the headers left aligned. The code itself is good and worked
# when I ran it on the codingame.
#
# tam670 I appreciated the suggestions, Drake. I really like the idea of having
# the comments at the begining of a code block, with the same indentation as the
# code. I think that you would be very satisfied with the changes that I
# implemented.

