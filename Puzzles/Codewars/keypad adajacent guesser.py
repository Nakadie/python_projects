# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:39:36 2021

@author: Kamuela
"""
import itertools

possible = {1:[1,2,4],
            2:[1,2,3,5],
            3:[2,3,6],
            4:[1,4,5,7],
            5:[2,4,5,6,8],
            6:[3,5,6,9],
            7:[4,7,8],
            8:[5,7,8,9,0],
            9:[6,8,9],
            0:[8,0]
            }
def get_pins(num):
    combo = []
    for i in str(num):
        if int(i) in possible:
            combo.append(possible.get(int(i)))
    final = list(itertools.product(*combo))
    final = ["".join(f"{elem}" for elem in tup) for tup in final]
    return final

print(get_pins(3))

# '11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]
        
    