# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:29:28 2021

@author: Kamuela
"""

def gcdRecur(b, a):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    else:
        return gcdRecur(a, b % a)
    

a= 462
b= 1071
print(gcdRecur(a, b))