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
"""
OUTPUT:

-------------------------------------------------------------
Sequential Odd Number Sums of (1 to N) Natural Number Squared 
-------------------------------------------------------------
1² = 1 = 1 

2² = 1 + 3 = 4 

3² = 1 + 3 + 5 = 9 

4² = 1 + 3 + 5 + 7 = 16 

5² = 1 + 3 + 5 + 7 + 9 = 25 

6² = 1 + 3 + 5 + 7 + 9 + 11 = 36 

7² = 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49 

8² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64 

9² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 = 81 

10² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100 

11² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 = 121 

12² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 = 144 

13² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 = 169 

14² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 = 196 

15² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 = 225 

16² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 = 256 

17² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 + 33 = 289 

18² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 + 33 + 35 = 324 

19² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 + 33 + 35 + 37 = 361 

20² = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 + 31 + 33 + 35 + 37 + 39 = 400 

-------------------------------------------------------------
********************** End of Program ***********************
-------------------------------------------------------------
"""
