def genPrimes():
    primes=[2]
    print (2)
    next_num = 3
    
    while True:
        temp_list = primes[:]
        if all(((next_num % prime) != 0) for prime in temp_list ):
        
            primes.append(next_num)
            print (next_num)
        
        next_num += 2  ## odds
        
        if len(primes) == 50:
             break
        

genPrimes()
