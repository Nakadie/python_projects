# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:00:28 2021

@author: Kamuela
"""
string = 'test'
def get_middle(s):
    midpoint = (len(s)/2)
    end = int(midpoint) + 1
    start = int(midpoint) - 1
    if len(s)%2 == 1:
        return s[int(midpoint)]
    else:
        return s[start:end]
print(get_middle(string))
    