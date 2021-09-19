# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:34:57 2021

@author: Kamuela
"""
string = 'Kamuela my Name'
def reverse_words_order_and_swap_cases(sent):
    
    split = sent.split(' ')
    rev = []
    final = []
    for i in split:
        rev.insert(0, i)
    for x in range(len(rev)):
        middle = []
        for i in rev[x]:
            
            upp = i
            if upp.isupper() == True:
                middle.append(upp.lower())
            else:
                middle.append(upp.upper())
        final.append(''.join(middle))
    return ' '.join(final)
        
        
        
    
    
    
print(reverse_words_order_and_swap_cases(string))
    