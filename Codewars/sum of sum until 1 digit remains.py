# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:30:50 2021

@author: Kamuela
"""

def digital_root(n):
    numbers = [int(x) for x in str(n)]
    
    while sum(numbers) > 9:
        n = sum(numbers)
        numbers = [int(x) for x in str(n)]
    else:
        return sum(numbers)
    
        




print(digital_root(81366852088))



# examples
# digital_root(16), 7)
# (digital_root(942), 6)
# (digital_root(132189), 6)
# (digital_root(493193), 2)



# best answer 
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))