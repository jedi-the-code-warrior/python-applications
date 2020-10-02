# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:25:55 2019

@author: Anjani K Shiwakoti

Synopsys: Counting (aggregating vowels in any corpus of text in English.)
"""

# create a string of vowels
vowels = "aeiou"

# initialize a dictionary with each vowel as a key and each value set to 0
count_dict = {}.fromkeys(vowels,0)
print("Initial Dictionary State: ", count_dict)

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

# make it suitable for caseless comparisions
text = text.casefold()
print("Transformed Text: ", text)

# keep a count of each vowel in the dictionary
for letter in text:
    if letter in vowels:
        count_dict[letter] += 1

print ("Final Dictionary State: ", count_dict)
    



