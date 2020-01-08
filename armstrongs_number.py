# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:25:55 2019

@author: Anjani K Shiwakoti

Detecting Armstrong's Number: abcd...n = a^n + b^n + c^n + d^n + ...
"""

import time
import numpy as np
 

def ArmstrongsNumber(num):
    
        digit_list = list(str(num))
        order = len(digit_list)
        expanded_sum_of_digits = 0
        
        for digit in digit_list:
            expanded_sum_of_digits += int(digit)**order 
        #print ("Sum of Each Digit^Order", expanded_sum_of_digits)
        
        if num == expanded_sum_of_digits:
            #print ("Found Armstrong's Number: ", number)
            return num
    
upper_limit = 1000000 # for easy testing
#int(input("Enter any positive integer up to which you want to detect Armstrong's Number: "))

start = time.time()    
for number in np.arange(1,upper_limit+1):
        
    if ArmstrongsNumber(number) != None:
        print (ArmstrongsNumber(number))    

end = time.time()        
        
print ("Run time: ", end-start)        
