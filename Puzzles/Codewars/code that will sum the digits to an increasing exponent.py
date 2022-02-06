# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:14:33 2021

@author: Kamuela
"""
able = []


def sum_dig_pow(a, b):# range(a, b + 1) will be studied by the function
    
    exp = 0
    x = range(a, b+1)
    n = str(x)
    count = 0
    p = 0
    for i in range(a, b+1):
        if i < 10:
            able.append(i)
        else:
            exp = 0
            count = 0
            p = 0
            n = str(i)
            for i in n:
                exp +=1
                p += int(i)**exp
            if p == int(n):
                able.append(p)
            else:
                pass
    return able


print(sum_dig_pow(1, 89))

#expected answer [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

#best 
def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))