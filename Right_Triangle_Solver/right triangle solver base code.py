# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:11:20 2021

@author: Nakadie
"""
import math
import matplotlib

#record inputs  
def get_values():
    values = {}
    variables = ['LenA', 'LenB', 'LenC', 'a', 'b']
    print('For triangel ABC LenA is opposite angle a, LenB is opposite angle b.\nAngle c is always 90º, lenC is the hypotenuse.')
    for name in variables:
        while True:
            try:
                user_input = input(f"Enter the value for {name}. If None, type None: ")
                if user_input.lower() == "none":
                    values[name] = None
                else:
                    values[name] = float(user_input)
            except ValueError:
                print("Error! This is not a number. Try again.")
                continue
            break
    values['c'] = 90       
    return values

#do math depending on what values I have    
def solve(values):
    if values['a'] == None and values['b'] == None:
        values['b'] = round(math.degrees(math.acos((values['LenA']/values['LenC']))), 2)
    if values['a'] == None: 
        values['a'] = 90 - values['b']
    elif values['b'] == None:
        values['b'] = 90 - values['a']
    if values['LenA'] == None and values['LenB'] == None:
        values['LenA'] = round(values['LenC'] * math.tan(math.radians(values['a'])), 2)
        values['LenB'] = round(values['LenC'] * math.cos(math.radians(values['a'])), 2)
    if values['LenA'] == None and values['LenC'] == None:
        values['LenA'] = round(values['LenB'] * math.tan(math.radians(values['a'])), 2)
        values['LenC'] = round(values['LenB'] / math.cos(math.radians(values['a'])), 2)
    if values['LenB'] == None and values['LenC'] == None:
        values['LenB'] = round(values['LenA'] * math.tan(math.radians(values['b'])), 2)
        values['LenC'] = round(values['LenA'] / math.cos(math.radians(values['b'])), 2)
    print('\n\n\nThe values of your triangle are:\n')   
    return print(values)
    


solve(get_values())