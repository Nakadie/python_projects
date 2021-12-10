#################################################
#################################################
#################################################
#this is broken code that does not work please ignore
#################################################
#################################################
#################################################

import collections
txt = open('D:\python_projects\Advent_of_code\day 3\puzzle.txt', 'r') 
txt = txt.read().splitlines()
#collections.counter

upper = []
lower = []
#separate into upper and lower lists
for i in range(1):
    count = []
    for j in txt:
        
        count.append(j[i])
    count = collections.Counter(count)
    if count['0'] > count['1']:
        for k in txt:
            if k[i] == '0':
                upper.append(k)
            else:
                lower.append(k)
                
    elif count['0'] < count['1']:
        for k in txt:
            if k[i] == '1':
                upper.append(k)
            else:
                lower.append(k)
            

#narrow down the upper list binary numbers one by one.
#first by finding the most common number either 1 or 0 then appending from there.
for i in range(12):
    count = []
    for j in upper:
        
        count.append(j[i])
    count = collections.Counter(count)
    if count['0'] > count['1']:
        for k in upper:
            if k[i] == '1':
                upper.remove(k)
    elif count['0'] <= count['1']:
        for k in upper:
            if k[i] == '0':
                upper.remove(k)
   
#narrow down the upper list binary numbers one by one.
#first by finding the most common number either 1 or 0 then appending from there.
for i in range(12):
    count = []
    for j in lower:
        
        count.append(j[i])
    count = collections.Counter(count)
    if count['0'] > count['1']:
        for k in lower:
            if k[i] == '0':
                lower.remove(k)
    elif count['0'] < count['1']:
        for k in lower:
            if k[i] == '1':
                lower.remove(k)
 

print(upper, lower)