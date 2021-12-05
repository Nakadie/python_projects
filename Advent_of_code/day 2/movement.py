txt = open('D:\python_projects\Advent_of_code\day 2\puzzle.txt', 'r') 
inst = txt.read().splitlines()
fullinst = []
x = 0
y = 0
for i in inst:
    fullinst.append(i.split())
for i in range(len(fullinst)):
    if fullinst[i][0] == 'forward':
        x += int(fullinst[i][1])
    elif fullinst[i][0] == 'up':
        y -= int(fullinst[i][1])
    elif fullinst[i][0] == 'down':
        y += int(fullinst[i][1])
print(x * y)