# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:47:01 2021

@author: Kamuela
"""

x = 39
def persistence(x):
    answer  = 1
    finanswer = 10
    numbers = []
    gen = 0
    if x <= 9:
        return 0
    while finanswer > 9:
        answer  = 1
        x = list(str(x))
        numbers = []
        for i in x:
            
            numbers.append(int(i))
        for i in numbers:
            answer = answer * i
            finanswer = answer
            x = answer
        gen +=1
    else:
        return gen

    
print(persistence(x))
# returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit
                 
                 
#best
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count