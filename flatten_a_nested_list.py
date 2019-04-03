# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 02:15:50 2019

@author: Anjani K Shiwakoti
Synopsis: Given a nested list, flatten any list within that list of size 1 (dimension) or deeper
"""

def flatten_a_nested_list(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # if and only if all elements are of size 1 (dimension) list type:
    # flattened_list = (sum(aList,[])) 
    
    # if size > 1 but all elements are of uniform (same) size then: 
    # iterate over the sizes until flattened usinf for loop
    
    # for everything else:
    
    newlist = []
    for item in aList:
         if isinstance(item, list):
             newlist = newlist + flatten(item)
         else:
             newlist.append(item)
    return newlist 
    
      
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten_a_nested_list(aList))

# OUTPUT: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
