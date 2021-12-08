import collections
txt = open('D:\python_projects\Advent_of_code\day 3\puzzle.txt', 'r') 
txt = txt.read().splitlines()
#collections.counter
final = []
upper = []
lower = []
for i in range(12):
    count = []
    for j in txt:
        
        count.append(j[i])
    count = collections.Counter(count)
    if count['0'] > count['1']:
        upper.append('0')
        lower.append('1')
    else:
        upper.append('1')
        lower.append('0')
print(''.join(upper), lower)
#print(int(''.join(upper), 2) * int(''.join(lower), 2))

