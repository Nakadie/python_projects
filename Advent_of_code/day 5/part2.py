# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
# Each position is shown as the number of lines which cover that point or . if no line covers that point.
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

#Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.


import collections
import numpy as np
txt = open('D:\python_projects\Advent_of_code\day 5\puzzle.txt', 'r')
txt = txt.read().splitlines()

txt = [x.split() for x in txt]
start = [x[0].split(',') for x in txt]
finish = [x[2].split(',') for x in txt]

vert_lines = []
hori_lines = []

for i in range(len(start)):
    if (int(start[i][0]) == int(finish[i][0])):
        vert_lines.append([int(start[i][0]), (sorted([int(finish[i][1]), int(start[i][1 ])]))])
    elif (int(start[i][1]) == int(finish[i][1])):
        hori_lines.append([int(start[i][1]), (sorted([int(finish[i][0]), int(start[i][0])]))])