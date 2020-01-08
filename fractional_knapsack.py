# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:47:34 2018

@author: Anjani K Shiwakoti
"""

def fractional_knapsack(C, w, v):
    """
    Inputs: floats of C: capacity, w: weights, v: values
    Outputs: a tuple of fractions, fitting_values
    """
    
    num_items = len(w)
    indices = list(range(num_items))
    fractions = [0]*num_items
    fitting_values = [0]*num_items
    
    ratios = [v/w for v,w in zip(v,w)]
    
    # sort indices in place
    indices.sort(key=lambda i: ratios[i], reverse=True)
    
    for index_ in indices:
        if w[index_] <= C:
            fractions[index_] = 1
            fitting_values[index_] = v[index_]
            C = C - w[index_]
        else:
            fractions[index_] = C/w[index_]
            fitting_values[index_] = fractions[index_] * v[index_]
    
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
