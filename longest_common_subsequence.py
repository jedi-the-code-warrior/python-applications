# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:12:29 2020

@author: Anjani K Shiwakoti


# Title: Longest Common Subsequence
# Package: algorithms
#
# Problem Statement:
# Given two sequences, find the longest common subsequence between them. 
# There can be gaps between elements in a single list (may not be contiguous) 
# but the order (sequence) of common elements in both the lists must be the same.
#
# Time Complexity: O(n*m)
# where m and n are the size of the input lists, respectively
#
# Sample Input: awaited, alpine
# Sample Output: aie
#
# DEFINITION OF SUBSEQUENCE:
# A sequence is a particular order in which related objects follow
# each other (e.g. DNA, Fibonacci). A sub-sequence is a sequence
# obtained by omitting some of the elements of a larger sequence.
#
# SEQUENCE       SUBSEQUENCE     OMISSION
# [3,1,2,5,4]     [1,2]            3,5,4
# [3,1,2,5,4]     [3,1,4]          2,5
#
# SEQUENCE       NOT SUBSEQUENCE   REASON
# [3,1,2,5,4]     [4,2,5]           4 should follow 5
#
# STRATEGY:
# An easy way to find a longest common subsequence of characters between
# two words is to first track the lengths of all the common sequences
# and then from those lengths pick a maximum; finally, from that
# maximum length, trace out the actual longest common subsequence
# between the two words.
#
# Let's use a table C (i.e. list C) to track the lengths of all common
# sub-sequences between the two input words. Naturally, C starts with
# all cells set to zero. Then to fill up C, we walk thru the two words,
# comparing characters. Each time we find a match, we mark the
# corresponding cell in C as one plus whatever maximum we had seen so
# far for that particular sub-sequence.
#
# When we are done filling up C, we find a maximum length z in C. Then
# using the indices of z, we trace that actual sequence and return it
# as the answer.
#
# The ensuing code shows the details of how we fill C and then from C
# extract the actual LCS.
#
#        ~~~~    ~~~~    ~~~~    ~~~~    ~~~~    ~~~~    ~~~~
#
# The remaining paragraphs contain details that you may not particularly
# care for. You may skip them and go right to the code.
#
# Finding the LCS of two sequences X and Y, i.e. LCS(X,Y), is similar
# in structure to finding the Fibonacci of some number n, i.e. fib(n).
# Both problems exhibit optimal substructures. Which is to say,
# for instance, the solution to fib(5) contains the solution to fib(4)
# which in turn contains fib(3), and so on. Similarly, the solution
# of LCS(X,Y) contains the solution of LCS(X-1,Y), which in turn
# contains the solution of LCS(X-1,Y-1), and so on. Whenever a problem
# exhibits "optimal substructure", we can use recursion to solve it:
#
#             _
#            | fib(n-1)+fib(n-2)    if n > 1
#   fib(n) = | n                    if n == 1 or n == 0
#            |_
#     
#
# For the LCS recurrence relation, a few notes are necessary:
# Let C(i,j) be the length of the prefix of LCS(X,Y) given by
#
#   C(i,j) = |LCS(X[1..i],Y[1..j])|
#
# so that if the length of X is m and the length of Y is n,
#
#   C(m,n) = |LCS(X,Y)|
#
# Then the recurrence relation for filling C is
#             _
#            | C(i-1,j-1)+1            if X(i) == Y(j)
#   C(i,j) = | max[C(i-1,j),C(i,j-1)]  otherwise
#            |_
#
# In addition to "optimal substructures", the LCS(X,Y) like the fib(n)
# contains overlapping subproblems.  What we mean is this: In solving
# f(5), we meet f(2) both as a subproblem of f(4) and as a subproblem
# of f(3).
#
#             fib(5)
#           /        \
#       fib(4)        fib(3)       :fib(5)=fib(4)+fib(3)
#       /    \       /     \
#   fib(3) fib(2)  fib(2)  fib(1)  :fib(5)=fib(3)+fib(2)+fib(2)+fib(1)
#
# Whenever a problem exhibits "overlapping subproblems", if you use
# recursion as a strategy you will end up solving the same subproblems
# more than once. Therefore, it makes more sense to track subproblems
# using a table so that once you solve a subproblem, you can simply
# lookup its solution next time you need.
#
# CONCLUSION:
# In the foregoing "strategy" section, we essentially described
# dynamic programming.
#
# Dynamic Programming: (aka Dynamic Tabling) is a strategy for solving
#   problems, which exhibit optimal substructures and overlapping
#   subproblems, by using a table to track the solution of subproblems
#   that have already been solved so as not to solve a subproblem more
#   than once. This tracking or note taking is usually referred to as
#   memoization, meaning writing in a memo.

#====================================================================
# Space Complexity: O(n*m)
# where m and n are the size of the input lists, respectively
#====================================================================
"""
#====================================================================  
# This solution first computes a table of lengths and then from that
# table computes an actual longest common subsequence.
#====================================================================

def LCS( A, B ):
    m = lcsTable( A, B )
    return actualLCS( m, A, B )
 
 
#=======================================================================
# LCS table of lengths
#=======================================================================
    
def lcsTable( A, B ):
    m = [[0 for y in range( len( B ) + 1 )] for x in range( len( A ) + 1 )]
    for x in range( 1, len( A ) + 1 ):
      for y in range( 1, len( B ) + 1 ):
        if A[x - 1] == B[y - 1]:
          m[x][y] = 1 + m[x - 1][y - 1]
        else:
          m[x][y] = max( m[x][y - 1], m[x - 1][y] )
 
    return m
 
#=======================================================================
# Extract an actual LCS from the length table, which effectively
# contains all the possible longest common sequences.
#=======================================================================
 
def actualLCS( m, A, B ):
    result = []
    x , y = len( A ), len( B )
    while x > 0 and y > 0:
      if A[x - 1] == B[y - 1]:
        result.append( A[x - 1] )
        x -= 1
        y -= 1
      elif m[x][y - 1] > m[x - 1][y]:
        y -= 1
      else:
        x -= 1
 
    return result  ### list in reversed order, why?

### driver code
listA = [3,0,5,6,9,11,1,7,2,4,8,-10]
listB = [0,4,8,6,11,9,1,7,2,3,-10,5]
result = [elem for elem in reversed(LCS(listA, listB))]
print(f"Longest common subsequence of {listA} and {listB} is: ", result)

### end of program