# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:11:31 2021

@author: Kamuela
"""

def number(bus_stops):
    return sum([x[0] - x[1] for x in bus_stops])
    
    
    
    
print(number([[10,0],[3,5],[5,8]]))



# data sets
# ([[10,0],[3,5],[5,8]]),5)
# ([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
# ([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)