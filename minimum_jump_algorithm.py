# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:57:27 2020

@author: Anjani k Shiwakoti

Synopsis: Minimum Jump From Start To Finish

The Problem: Given an array of non-negative integers, start from the first element 
and reach the last by jumping. The jump length can be at most the value at the current 
position in the array. The optimum result is when you reach the goal using a minimum number of jumps.
"""

def minJump(a):
    end=len(a)
    count=0
    i=a[0]
    tempList1=a
    while(i<=end):
        if(i==0):
            return 0
        tempList1=a[count+1:count+i+1]
        max_index=a.index(max(tempList1))
        count+=1
        i=a[max_index]
        end=end-max_index
    return count+1

print(minJump([3,0,4,1,2,2,0,0,1,2]))