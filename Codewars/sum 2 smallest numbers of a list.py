# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:44:43 2021

@author: Kamuela
"""
a1 = [5, 8, 12, 18, 22]
def sum_two_smallest_numbers(numbers):
    l1 = []
    numbers.sort()
    while len(l1) < 2:
        for i in numbers:
            if i < 0:
                pass
            if i >= 0:
                l1.append(i)
                numbers.remove(i)
                break
            
                
    return sum(l1)

print(sum_two_smallest_numbers(a1))
        
    