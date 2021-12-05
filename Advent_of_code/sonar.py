
txt = open('D:\python_projects\Advent_of_code\puzzle.txt', 'r') 
depths = txt.read().splitlines()
count = 0
for i in range(len(depths)):
    curdep = depths[i]
    if curdep < depths[i+1]:
        count  += 1
        print(count)
print(count)