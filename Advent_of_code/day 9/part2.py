import matplotlib.pyplot as plt
import numpy as np


txt = open('D:\python_projects\Advent_of_code\day 9\puzzle.txt', 'r')
txt = txt.read().splitlines()
depth = [list(x) for x in txt]
depth = [[int(x) for x in group] for group in depth]
depth = np.array(depth)
depth_chart = np.full((len(depth) + 2, len(depth[0])+2), 10, dtype=int)
values = []

for i in range(len(depth)):
    for j in range(len(depth[i])):
        depth_chart[i+1][j+1] = depth[i][j]

for i in range(1, len(depth_chart[1:])):
    for j in range(1, len(depth_chart[i][1:])):
        if depth_chart[i][j] < depth_chart[i-1][j] and depth_chart[i][j] < depth_chart[i+1][j] and depth_chart[i][j] < depth_chart[i][j-1] and depth_chart[i][j] < depth_chart[i][j+1]:
            values.append((i, j))
low_points = values
areas = []
current_area = []
def flood_fill(depth_chart, y, x):
    
    if depth_chart[y][x] < 9:
        depth_chart[y][x] = 10
        current_area.append((x,y))
        
        if x > 0:
            flood_fill(depth_chart, y, x-1)
        if x < len(depth_chart[y]) - 1:
            flood_fill(depth_chart, y, x+1)
        if y > 0:
            flood_fill(depth_chart, y-1, x)
        if y < len(depth_chart) - 1:
            flood_fill(depth_chart, y+1, x)
    else:
        return 
    


for i in low_points:
    y,x = i
    current_area = []
    flood_fill(depth_chart, y, x)
    areas.append(len(current_area))
areas.sort(reverse=True)
print(areas[0] * areas[1] * areas[2])


    


# print(low_points)
# a = depth
# plt.imshow(a, cmap='hot', interpolation='nearest')
# plt.show()












