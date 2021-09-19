# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:07:13 2021

@author: Kamuela
"""

high = 100
low = 0

print('lets play a guessing game')
print('is this your number? '+ str(round((high+low)/2)))

while True:
    command = input('''Please press 'l' if too low press 'h' if too high and press 'c' if correct!''')
    if command == 'c':
        print('your number is ' + str(round((high+low)/2)))
        break
    elif command == 'h':
        high = (abs(high+low)/2)
        print('is this your number? '+ str(round((high+low)/2)))
    elif command == 'l':
        low = (abs(high+low)/2)
        print('is this your number? '+ str(round((high+low)/2)))
    elif command not in {'l', 'h', 'c'}:
        print('''Please only enter 'l,c,or h' thank you.''')
print('thanks for playing')