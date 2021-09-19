# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:55:40 2021

@author: Kamuela
"""


def add_binary(a, b):
    a = int(a)
    b = int(b)
    binary = bin(a + b)
    return binary[2:-1]
    

print(add_binary(2, 2))

#best
def add_binary(a,b):
    return bin(a+b)[2:]