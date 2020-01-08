# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:47:34 2018

@author: Anjani K Shiwakoti
"""

def fractional_knapsack(W, w, v):
    """
    Inputs: floats of W: capacity, w: weights, v: values
    Outputs: a tuple of fractions, fitting_values
    """
    
    num_items = len(w)
    index = list(range(num_items))
    fractions = [0]*num_items
    fitting_values = [0]*num_items
    
    ratios = [v/w for v,w in zip(v,w)]
    
    index.sort(key=lambda i: ratios[i], reverse=True)
    
    
    for idx in index:
        if w[idx] <= W:
            fractions[idx] = 1
            fitting_values[idx] = v[idx]
            W = W - w[idx]
        else:
            fractions[idx] = W/w[idx]
            fitting_values[idx] = fractions[idx] * v[idx]
    
    return (fractions, fitting_values)

# test case
capacity = 99
weights = [10, 20, 40, 50]
values = [60, 100, 120, 200]

print ("Fitted weights with the maximum value = {}"
       .format(fractional_knapsack(capacity, weights, values)[1]))
print ("Fractions of the maximum weights fitted = {}"
       .format(fractional_knapsack(capacity, weights, values)[0]))
print ("Maximum value that can be fitted in Knapsack = {}"
       .format(sum(fractional_knapsack(capacity, weights, values)[1])))

###### OUTPUT ######
Fitted weights with the maximum value = [60, 100, 57.0, 200]
Fractions of the maximum weights fitted = [1, 1, 0.475, 1]
Maximum value that can be fitted in Knapsack = 417.0
