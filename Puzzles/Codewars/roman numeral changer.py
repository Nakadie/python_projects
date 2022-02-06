# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:50:14 2021

@author: Kamuela
"""

class RomanNumerals:
    def __init__(self, Numerals):
        self.Numerals
    Numerals = {'I': 1, 
                'II': 2,
                'III': 3,
                'IV': 4,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M':1000
                }
    def to_roman(num):
        # numeral = []
        # n = []
        # while num:
        #   num, x = divmod(num,10)
        #   if x:
        #     n.insert(0,x)
        
        
        # try 2
        # strnum = str(num)
        # number = []
        # final = []
        
        # for i in strnum:
        #     number.append(i)
        # for x in range(len(number)):
        #     final.insert(x, (str(number[x]) + ('0'* (len(range(len(number) - (x-1)))))))
        # return final
        
        #try 3
        numer = []
        while int(num) > 0:
            if num >= 1000:
                num -= 1000
                numer.append('M')
            elif num >= 500:
                num -= 500
                numer.append('D')
            elif num >= 100:
                 num -= 100
                 numer.append('C')
            elif num >= 50:
                 num -= 50
                 numer.append('L')
            elif num >= 10:
                 num -= 10
                 numer.append('X')
            elif num >= 5:
                 num -= 5
                 numer.append('V')
            elif num >= 4:
                 num -= 4
                 numer.append('IV')
            elif num >= 3:
                 num -= 3
                 numer.append('III')
            elif num >= 2:
                 num -= 2
                 numer.append('II')
            elif num >= 1:
                 num -= 1
                 numer.append('I')
        return ''.join(numer)
                 
                

    def from_roman(numeral):
        total = 0
        for i in numeral:
            if '6' in numeral
            total += RomanNumerals.Numerals[i]
        return total
    
    ##
    # numerals = 'XIV'
    # translate = {'I': 1, 'V': 5, 'X': 10} # i cant be bothered to write the rest
    # numerals = [*map(translate.get, numerals)]
    
    # for i, j in zip(numerals, numerals[1:]):
    #   if i < j:
    #     numerals[numerals.index(j)] -= 1
    #     numerals.pop(numerals.index(i))
    
    # print(sum(numerals))
    
    
    
print(RomanNumerals.to_roman(6)) #MCMXC