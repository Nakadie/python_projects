from collections import Counter


'([])' # valid
'((' # incomplete
'(])' # corrupt
txt = open('D:\python_projects\Advent_of_code\day 10\example.txt', 'r')
txt = txt.read().splitlines()
txt = [sorted(list(x)) for x in txt]
count = [Counter(x) for x in txt]
setlist = [set(x) for x in txt]
setlist = [''.join(x) for x in setlist]

print(count)