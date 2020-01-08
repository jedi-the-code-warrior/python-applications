# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:18:38 2019

@author: Anjani K Shiwakoti

Synopsis:
Calculate first N primes using generator function using bounded and unbounded methods.

"""

def genPrimes_unbounded():
    """
    This is my own method for generating N primes.
    """
    # all primes are odd numbers but the reverse is not true of primes
    # the number 5 and the multiples of 5 are special cases in primes
    # so start at 2, yield prime at current index and set next prime to 3
    primes=[2]
    yield primes[0]
    next_num = 3

    # for all other primes do ...
    while True: #len(primes) <= N:
        temp_list = primes[:]
        if all(((next_num % prime) != 0) for prime in temp_list ):
            yield (next_num)
            primes.append(next_num)
        next_num += 2  ## odds

# end of function

# Let how_many_primes be the number of primes we want to generate
how_many_primes = 50  ## int(input("How many prime numbers do you want to generate? ")

# calling the generator Nth times using its next() method
# for unbounded loop
primeGenerator = genPrimes_unbounded()
for num in range(how_many_primes): 
    print(primeGenerator.__next__())

print ("-" * 60)  ## separator line

## let's generate primes the other way around (bounded)
def genPrimes_bounded(N):
    """
    This is my own method for generating N primes.
    """
    primes=[2]
    
    yield primes[0]
    
    next_num = 3

    # for all other primes do ...
    while len(primes) < N:
        temp_list = primes[:]
        if all(((next_num % prime) != 0) for prime in temp_list ):
            yield (next_num)
            primes.append(next_num)
        next_num += 2  ## odds
        
# calling the generator Nth times using for loop  
# bounded loop    
for item in genPrimes_bounded(how_many_primes):
    print(item)
