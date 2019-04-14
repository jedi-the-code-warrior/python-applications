# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:37:07 2018

@author: Anjani K Shiwakoti

Synopsis:
    compute the square root of a positive number (float or integer) using Newton's method.
    Set Epsilon to any number of decimal places to get a better accuracy.
    
"""

def newton_sqrt(number, epsilon):
    
    # can handle positive numbers only
    if number < 0: 
        return "Number must be positive."
    
    # start with a guessed number    
    guess = 1.0
    
    # as long as the square of our guessed number minus the number is greater than 
    # the sufficiently small preset decimal value epsilon, keep guessing as follows:
    
    while abs((guess*guess)-number)>epsilon:
        
        # applying Newton's method for updating new value of guesses
        guess = (number/guess + guess)/2
        
    return guess

# TEST CASES
print (newton_sqrt(-1, 0.00001))
print (newton_sqrt(0, 0.00001))
print (newton_sqrt(99, 0.00001))
print (newton_sqrt(999999999, 0.00001))

# OUTPUT
Number must be positive.
0.001953125
9.949874371188393
31622.776585872405
