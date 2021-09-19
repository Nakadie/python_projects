# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:47:16 2021

@author: Kamuela
"""

def maskify(cc):
    mask = []
    for i in str(cc[0:-4]):
        mask.append('#')
    for i in str(cc[-4:len(cc)]):
        mask.append(i)
    return ''.join(mask)
       


print(maskify('im a potato man'))