txt = open('D:\python_projects\Advent_of_code\puzzle.txt', 'r') 
depths = txt.read().splitlines()
count = 0
for i in range(3, len(depths)):
    previous = int(depths[i-3]) + int(depths[i-2]) + int(depths[i-1])
    next = int(depths[i-2]) + int(depths[i-1]) + int(depths[i])
    print(previous, next)
    if previous < next:
        count +=1
print(count)