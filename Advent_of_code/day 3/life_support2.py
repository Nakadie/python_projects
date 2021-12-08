import collections
from typing import Counter
txt = open('D:\python_projects\Advent_of_code\day 3\puzzle.txt', 'r') 
txt = txt.read().splitlines()

upper = txt
lower = txt

if len(upper) != 1:
    for i in range(12):
        count = []
        for j in upper:
            
            count.append(j[i])
        count = collections.Counter(count)
        if len(upper) != 1:
            if count['1'] >= count['0']:
                upper = [x for x in upper if x[i] == '1']
            else:
                upper = [x for x in upper if x[i] == '0']
                
if len(lower) != 1:
    for i in range(12):
        count = []
        for j in lower:
            
            count.append(j[i])
        count = collections.Counter(count)
        if len(lower) != 1:
            if count['0'] <= count['1']:
                lower = [x for x in lower if x[i] == '0']
            else:
                lower = [x for x in lower if x[i] == '1']

        
print(int(upper[0], 2) * int(lower[0], 2))
