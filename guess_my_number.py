# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:46:59 2018

@author: AnjaniK Shiwakoti
"""

# guess my number between 0 and 100 (0 inclusive, 100 not inclusive)


low_val = 0
high_val = 100
flag = False
guess = 0
high_low = ""
print ("Please think of a number between 0 and 100!")
while flag == False:
    # set the intial value to guess variable
    # since guess can only range between 0 and 99, convert any fractions to int
    guess = int((low_val+high_val)/2)
    
    print ("Is your secret number " + str(guess) + "?")
    high_low = input("Enter 'h' to indicate the guess is too high." \
                     "Enter 'l' to indicate the guess is too low." \
                     "Enter 'c' to indicate I guessed correctly.")
    if high_low == 'h':
        high_val = guess
        flag == False
    elif high_low == 'l':
        low_val = guess
        flag == False
    elif high_low == 'c':
        flag == True
        print ("Game over. Your secret number was: " + str(guess))
        break    #if the answer is correct, exit the loop, end the program.
    else:
        flag == False
        high_low = print ("Sorry I don't recognize your answer!!" )
        # go back to top and ask again until user input is valid (h, l or c)

