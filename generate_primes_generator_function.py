# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:18:38 2019

@author: Anjani K Shiwakoti

Synopsis:
Calculate first N primes using generator function.

"""

def genPrimes_unbounded():
    
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
        

# Let how_many_primes be the number of primes we want to generate
how_many_primes = 50

# calling the generator Nth times using its next() method
# for unbounded loop
primeGenerator = genPrimes_unbounded()
for num in range(how_many_primes): 
    print(primeGenerator.__next__())

print ("__________________________________________________________________")


def genPrimes_bounded(N):
    
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
