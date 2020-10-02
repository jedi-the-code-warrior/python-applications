# -*- coding: utf-8 -*-
"""
Created on Sat Jan 2 14:19:59 2020

@author: Anjani K Shiwakoti

Title:
    Solving Maximum Subarray Problem using Kadane's Algorithm (Dynamic Programming)

Problem Definition: 
    Given a 1-dimensional array (or a collection) find the contiguous subarray having the maximum sum of its array elements. 

Constraints:
    1. The output subarray must be a contiguous array of elements (cannot skip any elements in the original array)
    2. The output subarray can have at least one element and at most ALL 'n' elements, the sum of which yields the highest number.
    3. If the array is empty, return None.

Approach:
    Dynamic Programming is an iterative/recursive process for solving a complex problem by breaking it down into a collection of 
    simpler subproblems, then solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map, etc.),
    which is refered to as memoization. So, the next time the same sub-problem occurs, instead of recomputing its solution, 
    one simply looks up the previously computed solution, thereby saving computation time.

How Does it Work:
    Consider an array of integers, A.  
    Start from the last element and calculate the sum of every possible subarray ending with the element A[n-1]. 
    Calculate the sum of every possible subarray ending with A[n-2], A[n-3] and so on up to A[0].
    For example, to calculate the local_maximum at, say, index 5, local_maximum[5], we don’t need to compute the sum of all subarrays 
    ending with A[5] since we already know the result from arrays ending with previous local maximum at index 4, A[4].

Intuition from Kadane's Algorithm:
    The local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.
    At every index i, the problem boils down to finding the maximum of just two numbers, A[i] and (A[i] + local_maximum[i-1]).
    Kadane's algorithm uses optimal substructures (the maximum subarray ending at each position is calculated in a 
    simple way from a related but smaller and overlapping subproblem: the maximum subarray ending at the previous position) this 
    algorithm can be viewed as a simple example of dynamic programming. Kadane’s algorithm is able to find the maximum sum of a 
    contiguous subarray in an array with a runtime of O(n) vs brute force approach which may take O(n^2).
"""

def MaxSumSubArray(xarray):
    """ Implements Kadane's Algorithm that finds contiguous substring with highest sum of its elements """
    
    ### temporarily set the local_max and global_max variables to negative infinity 
    ### so that when we are comparing max of two negative finite numbers, they're within the lower bound
    local_max  = float("-inf")
    global_max  = float("-inf")
    
    ### initialize an empty list to store our max sub array 
    max_sub_array = []
    
    def helper(sub_array, local_maximum,  global_maximum, max_sub_array):
        
        
        array_size = len(sub_array)
        
        if array_size == 0:
            return (max_sub_array, global_maximum)
        
        ### take the maximum sum of the two 
        local_maximum = max(sub_array[-1], sub_array[-1]+local_maximum)
        
        ### update the global maximum by resetting its value to the current local maximum        
        if local_maximum > global_maximum:
            global_maximum = local_maximum
             
        ### decrement the array size
        array_size = array_size - 1
        
        return helper(sub_array[:array_size], local_maximum,  global_maximum, max_sub_array)
        
    return helper(xarray, local_max, global_max, max_sub_array)


def main():
    
    # test array
    array = [10, 12, -17, 40, -20, 0, 6, -11, 0, -1, 4, 3, -40, 15, -2, 3]
    
    max_sum_sub_array, max_sum = MaxSumSubArray(array)
    
    print (f"THE MAXIMUM SUM OF CONTIGUOUS SUBARRAY = {max_sum}.")
    
    
if __name__=="__main__":
    main()