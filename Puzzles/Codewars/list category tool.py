# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:45:17 2021

@author: Kamuela
"""
data = [(45, 12),(55,21),(19, -2),(104, 20)]

def open_or_senior(data):
    division = []
    for key, value in data:
        if key >= 55 and value > 7:
            division.append('Senior')
        else:
            division.append('Open')
    return division

print(open_or_senior(data))
# expected
#['Open', 'Senior', 'Open', 'Senior']

#best
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]