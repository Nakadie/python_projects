# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:06:29 2021

@author: Kamuela
"""

import re

def to_camel_case(text):
    if '-' or '_' in text:    
        split = re.split('_|-', text)
        
        for i in range(1, len(split)):
            split[i] = split[i].capitalize()
        return print(''.join(split))
    else:
        return ''
        
        
        
    
    
    
    
to_camel_case('A-B_C')


# (''), '',
# "the_stealth_warrior"), "theStealthWarrior", 
# "The-Stealth-Warrior"), "TheStealthWarrior",
# "A-B-C"), "ABC", 