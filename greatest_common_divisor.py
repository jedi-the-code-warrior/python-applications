# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 02:26:52 2018

@author: Anjani K Shiwakoti
"""
# METHOD 1: USING ITERATION
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
   
    if a>b:
        bigger = a
        smaller = b
    else :
        bigger = b
        smaller = a
    # set the smaller number as divisor
    div = smaller
    if bigger % div == 0:
        return div
    else:
        # iterate throuh the divisor from high to low until we find the right div  
        while div >= 1:
            if div == 1:
                return 1
            if (smaller % div == 0) and (bigger % div == 0):
                return div
            div = div - 1
        
        # end of while loop
 
# test cases       
x1 = gcdIter(5, 15) 
print (x1)
x2 = gcdIter(16, 40)
print (x2)
x3 = gcdIter(27, 13) 
print (x3) 
x4 = gcdIter(11, 11) 
print (x4) 

#---------------------------------------------------------------------------------------------------------------------------------------
METHOD 2: USING RECURSION

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 02 14:11:49 2019

@author: AnjaniK Shiwakoti
"""

def gcdRecur(a, b):
    '''
    Input: a, b: positive integers
    
    Process: Using Euclid's method of calculating the greatest common divisor
    
    Output: Returns a positive integer, the greatest common divisor of a & b.
    '''
    
    # base case
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
