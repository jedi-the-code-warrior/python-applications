# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:57:43 2020

@author: Anjani K Shiwakoti

Synopsis: Function runtime calculator utility using decorators in Python
"""

import time

def decorator_fn(func):
    
    def wrapper(*args, **kwargs):
        print("Started executing function: [{}] ".format(func.__name__))
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        stop_time = time.time()
        print("Time to run: ", stop_time - start_time, " seconds.")
        print("Stopped execting function: [{}] ".format(func.__name__))
        return result
    
    return wrapper


@decorator_fn
def test_fn():
    time.sleep(5)  #let's say our test function took 5 seconds to run
    
test_fn()
"""
"""
@decorator_fn
def test_fn2(a, b, c, pi=3.1415, exp=2.718 ):
    total = a + b + c + pi + exp
    print("Sum of all numbers: ", total)
    
test_fn2(1,2,3)



import numpy as np
@decorator_fn
def test_fn3(**kwargs):
    keys = list(k for k,v in kwargs.items())
    vals = list(v for k,v in kwargs.items())
    print("Respective Square Roots: {} = {}".format(keys, np.sqrt(vals)))
    
test_fn3(pi=3.1416, exp=2.718, phi=1.618)

