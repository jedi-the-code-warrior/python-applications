# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:42:46 2020

@author: Anjani K Shiwakoti
"""
import numpy as np

def test_fn3(*args):
    
    vals = sum([v for v in args])
    print("Sum of all values in the keys: {} ".format(vals))

phi = (1 + np.sqrt(5))/2  # golden ratio
exp = np.e  # Euler's constant
pi = 4 * np.arctan(1)  # arctangent value of 1 in radians

test_fn3(pi, exp, phi)


def test_fn4(**kwargs):
    # calculating the natural logarithm (log to the base 2) of each value in the key of a dictionary
    dict_1= {k:np.log(v) for (k,v) in kwargs.items()}
    
    ## using list strips the dict_keys and dict_values from output
    print("Natural Log of each value in the keys: {} = {}".format(list(dict_1.keys()), list(dict_1.values())))
    
    # taking the square root of each value in the key of a dictionary
    dict_2= {k:np.sqrt(v) for (k,v) in kwargs.items()}
    
    ## using list strips the dict_keys and dict_values from output
    print("Respective Square Roots: {} = {}".format(list(dict_2.keys()), list(dict_2.values())))
    
test_fn4(pi=3.1416, exp=2.718, phi=1.618)
