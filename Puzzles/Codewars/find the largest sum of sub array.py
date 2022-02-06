# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:14:33 2021

@author: Kamuela
"""
a1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_sequence(arr):
    low = 0
    high = low + 1
    highscore = 2
    loop = 0
    score = sum(arr[low:high])
    if all(i < 0 for i in arr):
        return 0
    elif arr == None or arr == []:
        return 0
    else:
        while loop <= 2:
            if high < len(arr) + 1:
                score = sum(arr[low:high])
                if sum(arr[low:high]) > highscore:
                    highscore = sum(arr[low:high])
                    hsl = low
                    hsh = high
                elif low < high:
                    low += 1
                    score = sum(arr[low:high])
                elif low == high:
                    low = 0
                    high +=1
                
            else:
                loop += 1
                high = low + 1
    return sum(arr[hsl:hsh])
            
                
            
print(max_sequence(a1))
#answer should be 6: [4, -1, 2, 1]

#best answer
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max



    