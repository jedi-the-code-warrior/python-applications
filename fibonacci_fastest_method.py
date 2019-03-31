# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 07:40:57 2019

@author: Anjani K Shiwakoti

Synopsys: 
This program gets first N number of Fibonacci numbers and displays them sequentially in a list.
It explores multiple ways to solving this problem and see which algorithm is the best solution 
in terms of time complexity measures (efficiency).

"""

"""
Created on Sun Mar 31 02:28:59 2019

@author: Anjani K Shiwakoti

Synopsis: Implement dynammic programming technique in order to optimize the number 
of operations in calculating N number of Fibonacci in sequence using recursion.

How it works is that we trade time for space by not repeating what we have already calculated. 
We create a memo table of what we have calculated. We start with an empty table of dict. Before we 
calculate fib (n) we check to see if there's already a value of fib (n) stored in the table. If there is, 
then we look it up and simply re-use it. If not, then we calculate it and add it to the memo table.

"""
# THE VERY BEST METHOD (FAST AND ELEGANT)

def fastFibonacci(n, memo_dict={}):
    """ 
    Using dynamic programming technique (memoization), 
    calculates n-th Fibonacci number
    
    """
    # base case
    if n == 0 or n == 1:
        return 1
    
    # try to return the value of n in the table (memo dictionary)
    # if the value is there, we return it, and if not there then
    # we return a key error and then calculate the new value
    try:
        return memo_dict[n]
    
    except KeyError:
        
        # since table does not contain that value, calculate the new value
        fibonacci_list = fastFibonacci(n-1, memo_dict) \
                       + fastFibonacci(n-2, memo_dict)
        
        # add the new value to the table
        memo_dict[n] = fibonacci_list
        
        return fibonacci_list
        
# Now let's print out the result for N number of Fibonaccis in sequence    
N = 120
for n in range(N+1):
    print (n, "th Fibonacci = ", fastFibonacci(n))

    
# ----------------------------------OTHER METHODS------------------------------------------------

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
   

### METHOD 3
# this recursive method is pretty elegant but not recommended because of time complexity O(n^2)
# the best method is to implement 'memoization' technique from dynamic programming 

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

# This is very slow, seems to freeze around 40
N = 100        
print("The {}-th Fibonacci number is: {}".format(N,CalculateFibonacci(N)))   

####################################################################################################    

"""
Output of the best method up top:
----------------------------------------------------------------------------------------------------
0 th Fibonacci =  1
1 th Fibonacci =  1
2 th Fibonacci =  2
3 th Fibonacci =  3
4 th Fibonacci =  5
5 th Fibonacci =  8
6 th Fibonacci =  13
7 th Fibonacci =  21
8 th Fibonacci =  34
9 th Fibonacci =  55
10 th Fibonacci =  89
11 th Fibonacci =  144
12 th Fibonacci =  233
13 th Fibonacci =  377
14 th Fibonacci =  610
15 th Fibonacci =  987
16 th Fibonacci =  1597
17 th Fibonacci =  2584
18 th Fibonacci =  4181
19 th Fibonacci =  6765
20 th Fibonacci =  10946
21 th Fibonacci =  17711
22 th Fibonacci =  28657
23 th Fibonacci =  46368
24 th Fibonacci =  75025
25 th Fibonacci =  121393
26 th Fibonacci =  196418
27 th Fibonacci =  317811
28 th Fibonacci =  514229
29 th Fibonacci =  832040
30 th Fibonacci =  1346269
31 th Fibonacci =  2178309
32 th Fibonacci =  3524578
33 th Fibonacci =  5702887
34 th Fibonacci =  9227465
35 th Fibonacci =  14930352
36 th Fibonacci =  24157817
37 th Fibonacci =  39088169
38 th Fibonacci =  63245986
39 th Fibonacci =  102334155
40 th Fibonacci =  165580141
41 th Fibonacci =  267914296
42 th Fibonacci =  433494437
43 th Fibonacci =  701408733
44 th Fibonacci =  1134903170
45 th Fibonacci =  1836311903
46 th Fibonacci =  2971215073
47 th Fibonacci =  4807526976
48 th Fibonacci =  7778742049
49 th Fibonacci =  12586269025
50 th Fibonacci =  20365011074
51 th Fibonacci =  32951280099
52 th Fibonacci =  53316291173
53 th Fibonacci =  86267571272
54 th Fibonacci =  139583862445
55 th Fibonacci =  225851433717
56 th Fibonacci =  365435296162
57 th Fibonacci =  591286729879
58 th Fibonacci =  956722026041
59 th Fibonacci =  1548008755920
60 th Fibonacci =  2504730781961
61 th Fibonacci =  4052739537881
62 th Fibonacci =  6557470319842
63 th Fibonacci =  10610209857723
64 th Fibonacci =  17167680177565
65 th Fibonacci =  27777890035288
66 th Fibonacci =  44945570212853
67 th Fibonacci =  72723460248141
68 th Fibonacci =  117669030460994
69 th Fibonacci =  190392490709135
70 th Fibonacci =  308061521170129
71 th Fibonacci =  498454011879264
72 th Fibonacci =  806515533049393
73 th Fibonacci =  1304969544928657
74 th Fibonacci =  2111485077978050
75 th Fibonacci =  3416454622906707
76 th Fibonacci =  5527939700884757
77 th Fibonacci =  8944394323791464
78 th Fibonacci =  14472334024676221
79 th Fibonacci =  23416728348467685
80 th Fibonacci =  37889062373143906
81 th Fibonacci =  61305790721611591
82 th Fibonacci =  99194853094755497
83 th Fibonacci =  160500643816367088
84 th Fibonacci =  259695496911122585
85 th Fibonacci =  420196140727489673
86 th Fibonacci =  679891637638612258
87 th Fibonacci =  1100087778366101931
88 th Fibonacci =  1779979416004714189
89 th Fibonacci =  2880067194370816120
90 th Fibonacci =  4660046610375530309
91 th Fibonacci =  7540113804746346429
92 th Fibonacci =  12200160415121876738
93 th Fibonacci =  19740274219868223167
94 th Fibonacci =  31940434634990099905
95 th Fibonacci =  51680708854858323072
96 th Fibonacci =  83621143489848422977
97 th Fibonacci =  135301852344706746049
98 th Fibonacci =  218922995834555169026
99 th Fibonacci =  354224848179261915075
100 th Fibonacci =  573147844013817084101
101 th Fibonacci =  927372692193078999176
102 th Fibonacci =  1500520536206896083277
103 th Fibonacci =  2427893228399975082453
104 th Fibonacci =  3928413764606871165730
105 th Fibonacci =  6356306993006846248183
106 th Fibonacci =  10284720757613717413913
107 th Fibonacci =  16641027750620563662096
108 th Fibonacci =  26925748508234281076009
109 th Fibonacci =  43566776258854844738105
110 th Fibonacci =  70492524767089125814114
111 th Fibonacci =  114059301025943970552219
112 th Fibonacci =  184551825793033096366333
113 th Fibonacci =  298611126818977066918552
114 th Fibonacci =  483162952612010163284885
115 th Fibonacci =  781774079430987230203437
116 th Fibonacci =  1264937032042997393488322
117 th Fibonacci =  2046711111473984623691759
118 th Fibonacci =  3311648143516982017180081
119 th Fibonacci =  5358359254990966640871840
120 th Fibonacci =  8670007398507948658051921

"""
