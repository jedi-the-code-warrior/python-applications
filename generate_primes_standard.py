"""
Published: March 7, 2019
Author: Anjani K Shiwakoti
Synopsis: Generate N prime numbers sequentially and display the list.

"""
def genPrimes(N):
    primes=[2]
    print (2)
    next_num = 3
    
    while len(primes)<N:
        temp_list = primes[:]
        if all(((next_num % prime) != 0) for prime in temp_list ):
        
            primes.append(next_num)
            print (next_num)
        
        next_num += 2  ## odds
        
N= 1000
genPrimes(N)
