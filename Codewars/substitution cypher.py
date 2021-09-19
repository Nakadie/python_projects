# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:22:04 2021

@author: Kamuela
"""
message = 'Codewars'
def rot13(message):
    x = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lm = message.lower()
    code = []
    for x in range(len(message)):
        if lm[x] in alphabet:
            location = alphabet.index(lm[x])
            
            if location + 13 < len(alphabet):
                location = location + 13
                code.append(alphabet[location])
            else:
                location = (location + 13) - 26
                code.append(alphabet[location])
        else:
            code.append(lm[x])
    strcode = str(''.join(code))
    for x in range(len(message)):
        if message[x].isupper() == True:
            strcode = strcode.replace(strcode[x], strcode[x].upper(), 1)
        
        
        
            
            
            
    return strcode


print(rot13('10+2 is twelve.'))
#expected "Pbqrjnef"