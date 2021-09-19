# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:01:35 2021

@author: Kamuela
"""
list1 = [ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] 
def same_structure_with_zeroes(original):
  if isinstance(original, list):
    return [same_structure_with_zeroes(x) for x in original]
  return 0
def same_structure_as(original,other):
    return same_structure_with_zeroes(original) == same_structure_with_zeroes(other)
    
    
    
print(same_structure_as([ 1, [ 1, 1 ] ], [ 1, [ 1, 1 ] ]))