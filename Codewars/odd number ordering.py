# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:18:27 2021

@author: Kamuela
"""

a1 = [5, 3, 2, 8, 1, 4]
def sort_array(source_array): 
    odd = []
    for i in source_array:
        if i%2 == 1:
            odd.append(i)
    odd.sort()
    location = 0
    for i in source_array:
        if i%2 == 1:
            source_array.insert(location, odd[0])
            del source_array[location + 1]
            del odd[0]
            location += 1
        else:
            location += 1
    return source_array
print(sort_array(a1))


#number 1 answer
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
            