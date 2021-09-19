# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:10:57 2021

@author: Kamuela
"""
a2 = [121, 361, 361, 361, 14641, 20736, 20736, 25921]
a1 = [-161, -144, -144, -121, -11, 19, 19, 19]
def comp(array1, array2):
    if array1 == None:
        return False
    elif array2 == None:
        return False
    else:
        pass
    ab1 = [abs(ele) for ele in array1]
    ab2 = [abs(ele) for ele in array2]
    ab1.sort()
    ab2.sort()
    squareda1 = []
    for i in ab1:
        squareda1.append((i**2))
    if ab2 == squareda1:
        
        print(array2)
        print(squareda1)
        return True
    else:
        print(array2)
        print(squareda1)
        return False
print(comp(a1, a2))