# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:52:54 2021

@author: Kamuela
"""
lst = []
def first_non_repeating_letter(string):
    lst = []
    chars = string.lower()
    check_string = string.lower()
    
    if string == '':
        return ''
    if string == None:
        return ''
    
    for char in chars:
      count = check_string.count(char)
      if count > 1:
        lst.append(char)
      else:
          lst.append(0)
          
    for i in lst:
        if i == 0:
            location = lst.index(i)
            return string[location]
    for i in lst:
        if i != 0:
            return ''
        
    
print(first_non_repeating_letter('sss'))


#best solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""