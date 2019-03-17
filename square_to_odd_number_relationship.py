# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:56:25 2019

@author: Anjani K Shiwakoti
"""

#import numpy as np

def squareToOddNumbers(N):
    
    """
    The square of any finite natural number N is equal to the sum of all odd numbers 
    of the same size counted from 1 up to the N-th odd number in sequential order. 
    For example, the 7² is equal to the sum of the first 7 odd numbers in sequence, 
    i.e., 1 + 3 + 5 + 7 + 9 + 11 + 13. Same holds true for all finite natural numbers.
    """
    
    print("-------------------------------------------------------------")
    print("Sequential Odd Number Sums of (1 to N) Natural Number Squared ")
    print("-------------------------------------------------------------")

    
    
    for n in range(1,N+1):
        
        odd_sum_list = []
        odd_sum_string = ''
        
        for x in range(1, 2*n, 2):
            
            odd_sum_list.append(x)
            
            if sum(odd_sum_list) != n**2 :
                 odd_sum_string = odd_sum_string + str(x) + " + "
            else:
                odd_sum_string = odd_sum_string + str(x)
                break
                
        print("{}\u00b2 = {} = {} \n".format(n, odd_sum_string, sum(odd_sum_list)))    
    
    print("-------------------------------------------------------------")
    print("********************** End of Program ***********************")
    print("-------------------------------------------------------------")

    

squareToOddNumbers(20)