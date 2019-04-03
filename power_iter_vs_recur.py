# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 19:21:15 2018

@author: Anjani K Shiwakoti
"""

# METHOD 1: Using Recursion

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # base case
    if exp == 0:
        return 1
    
    # base^exp = base * base^(exp-1)
    return base * recurPower(base,exp-1)



# METHOD 2: Using Iteration

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    total = 1
    while exp >= 0:
        if exp == 0:
            return total 
            
        # multiply current total by base and 
        # update that value to as the new total
        total *= base
        # decrement exponent by 1   
        exp -= 1
    ### end of while loop 
