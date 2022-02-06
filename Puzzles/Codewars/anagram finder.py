# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:13:50 2021

@author: Kamuela
"""

def anagrams(word, words):
    sortword = ''.join(sorted(word))
    bigdict = []
    for x in words:
        bigdict.append(''.join(sorted(x)))
    finallst = [x for x in bigdict if x == sortword]
    return finallst
    
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# expected answer ['aabb', 'bbaa']