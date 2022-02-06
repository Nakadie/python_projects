import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    n=1
    while n%2 != 0:
        n = random.randint(1, 100)
        
        if n%2 == 0:
            return n
        
try1 = print(genEven())