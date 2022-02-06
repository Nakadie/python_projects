
txt = open('D:\python_projects\Advent_of_code\puzzle.txt', 'r') 
depths = txt.read().splitlines()
count = 1
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        print(depths[i-1], depths[i])
        count  += 1
        print(count)


