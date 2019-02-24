# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 04:34:47 2019

@author: Anjani K Shiwakoti
"""

# initialize all variables
index = 0
count = 0
alfa_substring = ""
alfa_substring_list = []
longest_substring = ""
longest_substring_list = []
ordered = False

# get the input string argument passed in to this program  
# and assign the input string to the local variable 
# add an extra character at the end of input string to prevent index overflow
input_string = s + "#" 

while index < (len(input_string)-1):
    
    if (str(input_string[index+1]) >= str(input_string[index])): 
        
        if count == 0:
            alfa_substring = alfa_substring + input_string[index]  
            ordered = True
            count = count + 1
        
        if count > 0 :
            alfa_substring = alfa_substring + input_string[index+1] 
            ordered = False
            count = count + 1
        
        # put each substring on a list for later processing
        alfa_substring_list.append(alfa_substring)
        
        
    else:
        # in case there are no letters in alphabetical order
        alfa_substring = input_string[index] 
        alfa_substring_list.append(alfa_substring)
        
        # empty the substring for the next iteration
        alfa_substring = ""
        ordered = False
        count = 0  
         
    index = index + 1   
# end of while loop


# find the substring with maximum length in the list

longest_count = max(map(len, alfa_substring_list))

# iterate thru the list to see which element(s) has/have that max length
# put all substrings that have matching max lengths in a list and
# then pick the first one from the list as output (first element = index 0)

for element in alfa_substring_list:

    if (len(element)==longest_count):
       longest_substring_list.append(element)
       
longest_substring = longest_substring_list[0]
print('Longest substring in alphabetical order is: ' + str(longest_substring))
# end of program