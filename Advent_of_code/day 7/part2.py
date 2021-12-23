from collections import Counter
txt = open('D:\python_projects\Advent_of_code\day 7\puzzle.txt', 'r')
txt = txt.read().splitlines()
txt = txt[0].split(',')
crabs = [int(x) for x in txt]

sums = []
for i in range(min(crabs), max(crabs) + 1):
    differences = []
    for crab in crabs:
        x = abs(crab - i)
        differences.append((x**2 + x)/2)
    sums.append(sum(differences))
for i in range(len(sums)):
    if sums[i] == min(sums):
        print(i, min(sums))