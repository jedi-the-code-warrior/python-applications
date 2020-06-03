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

#---------------------------------------------------------------------------------------------------------------------------------------
METHOD 3: USING RECURSION TO FIND GENERALIZED GCD FOR A LIST OF N POSITIVE INTEGERS
    
def generalizedGCD(num, arr):
    """
    Computes the greatest common divisor(GCD) or highest common factor(HCF)
    Input: 
           num - an int representing the number of positive integers (N)
           arr - a list of positive integers
           
    Output:
            returns an integer representing the GCD or HCF of the given positive integers
    
    """
    # edge cases
    
    # if list is empty
    if num == 0:
        return None 
    
    # if list contains single element     
    if num == 1:
        return arr[0]
    
    # if list contains a zero, avoid division by zero by returning None
    if any(arr) == 0:
        return None
    
    # helper function to compute GCD for all else 
    def GCDRecur(a, b):
        """ recursion method to compute GCD """
        
        # base case
        if b == 0:
            return a 
        else:
            return GCDRecur(b, a%b)
    
    # take an adjacent pair at a time and compute their GCD, 
    # keep track of their GCD on a list and move next until all pairs are visited
    # then return the minimun of the list of GCD's as our final result
    result_list = []
    for i in range(num-1):
        result = GCDRecur(arr[i],arr[i+1])
        result_list.append(result)
        
    #print(result_list)
    return min(result_list)
        
        
