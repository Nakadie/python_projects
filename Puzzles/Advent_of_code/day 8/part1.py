txt = open('D:\python_projects\Advent_of_code\day 8\puzzle.txt', 'r')
txt = txt.read().splitlines()


txt = [x.split(' ') for x in txt]


count = 0
for code in txt:
    #print(code)
    for word in code[11:15]:
        #print(len(word))
        if len(word) in [2, 3, 4, 7]:
            count += 1
            #print('count',count)

print(count)