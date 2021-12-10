import collections
txt = open('D:\python_projects\Advent_of_code\day 4\puzzle.txt', 'r') 
txt = txt.read().splitlines()

drawn_nums = [txt[0]]
boards = []
while True:
    temp = []
    while len(temp) != 5:
        for i in txt:
            if i == '':
                pass
            else:
                temp.append(i)


    
    
print(txt)