# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 07:40:57 2019

@author: Anjani K Shiwakoti

Synopsys: 
This program gets first N number of Fibonacci numbers and displays them sequentially in a list.
It explores multiple ways to solving this problem and see which algorithm is the best solution 
in terms of time complexity measures (efficiency).

"""

### METHOD 1
# this recursive method is pretty elegant but not recommended because of time complexity O(n^2)

"""
def CalculateFibonacci(N):
    """ 
    Get first N number of Fibonacci numbers and display them sequentially in a list 
    """
    
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return (CalculateFibonacci(N-1) + CalculateFibonacci(N-2))

N = 100        
print("The {}-th Fibonacci number is: {}".format(N,CalculateFibonacci(N)))   
"""
    
"""
#### METHOD 2
# here's a classic algorithm with time complexity O(n), that is linear

def CalculateFibonacci(N):
    """ 
    Get first N number of Fibonacci numbers and display them sequentially in a list 
    """
    
    print("------------------------------------------------------------------------")
    print("List of the First {} Fibonacci Numbers".format(N))
    print("------------------------------------------------------------------------")
 
    fibonacci = 0
    prev_num = 0
    next_num = 1
    fibonacci_list=[0,1]
    
    for n in range(N-1):
        
        fibonacci = prev_num + next_num
        prev_num = next_num 
        next_num = fibonacci
        fibonacci_list.append(fibonacci)
        
    return (fibonacci_list[:N])

        
print (CalculateFibonacci(100)) 
"""

### METHOD 3 (my own method)
# the following uses different logic but better still   

def CalculateFibonacci(N):
    """ 
    Get first last two numbers from the list of Fibonacci numbers, then add them to obtain the
    next Fibonacci number in the sequence and then append that number to the end of the list.
    Repeat this process until the desired number of Fibonaccis is reached.
    """
    
    print("------------------------------------------------------------------------")
    print("List of the First {} Fibonacci Numbers".format(N))
    print("------------------------------------------------------------------------")
 
    
    
    next_num = 0
    fibonacci = [0,1]
    
    while len(fibonacci) < N:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
        
    print (fibonacci)
        
CalculateFibonacci(100)      
   
"""
Output:
------------------------------------------------------------------------
List of the First 100 Fibonacci Numbers
------------------------------------------------------------------------
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 
4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 
832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 
63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 
2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 
86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 
1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 
27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 
308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 
3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 
37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 
420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 
4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 
31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 
218922995834555169026]

"""
