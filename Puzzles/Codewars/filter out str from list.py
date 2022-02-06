# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:41:28 2021

@author: Kamuela
"""
l = [1,2,'a','b']
def filter_list(l):
    integer = []
    for i in l:
      if isinstance(i, int) == True:
          integer.append(i)
    return integer

print(filter_list(l))
          
#best
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
          