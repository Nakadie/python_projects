txt = open('D:\python_projects\Advent_of_code\day 10\example.txt', 'r')
txt = txt.read().splitlines()
txt = [list(x) for x in txt]
setlist = [set(x) for x in txt]
print(setlist)