# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:13:59 2021

@author: Kamuela
"""
def permutations(string):
    import random
    import math
    lenstr = len(string)
    fact = math.factorial(lenstr)
    
    permutations = []
    loop = 0
    while loop <= fact* 2:
        bull = ''.join(random.sample(string, lenstr))
        if bull not in permutations:
            permutations.append(bull)
            loop += 1
            
        else:
            pass
            loop += 1
            
    return permutations
   


print(permutations('gypyfcv'))


# ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']