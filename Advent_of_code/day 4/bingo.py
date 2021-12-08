import collections
txt = open('D:\python_projects\Advent_of_code\day 4\puzzle.txt', 'r') 
txt = txt.read().splitlines()

drawn_nums = [txt[0]]
boards = []
for i in range(1, len(txt)):
    single = []
    
print(drawn_nums)