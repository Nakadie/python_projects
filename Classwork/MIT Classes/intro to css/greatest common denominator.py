# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:55:58 2021

@author: Kamuela
"""

def gcdIter(a, b):
    def isInteger(n):
        """Return True if argument is a whole number, False if argument has a fractional part.
    
        Note that for values very close to an integer, this test breaks. During
        superficial testing the closest value to zero that evaluated correctly
        was 9.88131291682e-324. When dividing this number by 10, Python 2.7.1 evaluated
        the result to zero"""
    
        if n%2 == 0 or (n+1)%2 == 0:
            return True
        return False
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a and b == 0:
        return 0
    elif a >= b:
        high = a
        low = b
        div = low
        while div>=1:
            if isInteger(high/div) and isInteger(low/div) == True:
                return div
            else:
                div -= 1
    elif a <= b:
        high = b
        low = a
        div = low
        while div>=1:
            if isInteger(high/div) and isInteger(low/div) == True:
                return div
            else:
                div -= 1
   
        
                
                
a = 16
b = 16
print(gcdIter(a, b))