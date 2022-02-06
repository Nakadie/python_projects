# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:24:40 2021

@author: Kamuela
"""
def middle_permutation(x):
    result = ""
    letters = list(x)
    letters.sort()
    if len(letters)%2 == 0:
        result += letters.pop(int(len(letters)/2)-1)
        for i in range(len(letters)):
            result += letters[len(letters) -1 - i]
    else:
        result += letters.pop(int((len(letters)-1)/2))
        result += middle_permutation("".join(letters))
    return result

print(middle_permutation('abcdxgz'))

# a letter with x letters has x! permutationsd
# 4 letters, 24. we need 12th word
# that's the last permutation of 2nd letter
# that means -- to get middle term of a even lettered word -- All you need to do is --
# Take the letter at n/2 position
# then order everything else from highest to lowest
# To get the middle term of an odd lettered word:
# - Take the alphabetically middle letter first, pop it
# - and use previous logic for even word