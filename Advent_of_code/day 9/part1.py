
import numpy as np


txt = open('D:\python_projects\Advent_of_code\day 9\puzzle.txt', 'r')
txt = txt.read().splitlines()
depth = [list(x) for x in txt]
depth = [[int(x) for x in group] for group in depth]
depth = np.array(depth)
depth_chart = np.full((len(depth) + 2, len(depth[0])+2), 100, dtype=int)
values = []


for i in range(len(depth)):
    for j in range(len(depth[i])):
        depth_chart[i+1][j+1] = depth[i][j]

for i in range(1, len(depth_chart[1:])):
    for j in range(1, len(depth_chart[i][1:])):
        if depth_chart[i][j] < depth_chart[i-1][j] and depth_chart[i][j] < depth_chart[i+1][j] and depth_chart[i][j] < depth_chart[i][j-1] and depth_chart[i][j] < depth_chart[i][j+1]:
            values.append(depth_chart[i][j])
        


# for i in range(len(depth)):
#     print(i)
#     for j in range(len(depth[i])):
#         if i == 0 and j == 0 :
#             if depth[i][j] < depth[i][j+1] and depth[i][j] < depth[i+1][j]:
#                 print('true')
#         if i == 0:
#             if depth[i][j] < depth[i][j-1] and depth[i][j] < depth[i][j+1] and depth[i][j] < depth[i+1][j]:
#                 print('true')
#         if j == 0:
#             if depth[i][j] < depth[i][j+1] and depth[i][j] < depth[i+1][j] and depth[i][j] < depth[i-1][j]:
#                 print('true')
#         if i == len(depth) and j == len(depth[i]):
#             if depth[i][j] < depth[i-1][j-1] and depth[i][j] < depth[i][j-1]:
#                 print('true')
#         if i == len(depth):
#             if depth[i][j] < depth[i][j-1] and depth[i][j] < depth[i-1][j-1]:
#                 print('true')
#         else:
#             if depth[i][j] < depth[i-1][j] and depth[i][j] < depth[i+1][j] and depth[i][j] < depth[i][j-1] and depth[i][j] < depth[i][j+1]:
#                 print('true')

print(sum(values)+len(values))


