# Write a generator, genPrimes, that returns the sequence of prime numbers on 
# successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 
# Have the generator keep a list of the primes it's generated. 
# A candidate number x is prime if (x % p) != 0 for all earlier primes p.






def genPrimes():
    primes = [2]
    x = 0
    while True:
        for p in primes:
            if x == 1:
                x += 2
                yield 2
            elif (x % p) == 0:
                x += 1
                break
            else:
                if p == primes[-1] and (x % p) != 0 and x != 1:
                    yield x
                    primes.append(x)
                    


foo = genPrimes()
print(foo.__next__())
            

########################### instructor answer#############################
# def genPrimes():
#     primes = []   # primes generated so far
#     last = 1      # last number tried
#     while True:
#         last += 1
#         for p in primes:
#             if last % p == 0:
#                 break
#         else:
#             primes.append(last)
#             yield last
    

    
