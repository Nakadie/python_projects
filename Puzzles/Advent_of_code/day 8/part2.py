from collections import Counter
txt = open('D:\python_projects\Advent_of_code\day 8\example.txt', 'r')
txt = txt.read().splitlines()
txt = [x.split(' ') for x in txt]


# x8 = Counter('acedgfb')
# x5 = Counter('cdfbe')
# x2 = Counter('gcdfa')
# x3 = Counter('fbcad')
# x7 = Counter('dab')
# x9 = Counter('cefabd')
# x6 = Counter('cdfgeb')
# x4 = Counter('eafb')
# x0 = Counter('cagedb')
# x1 = Counter('ab')

# numbers = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]

numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

number_board = [[],
                [],
                [],
                [],
                []
                ]

# sum = 0
# for code in txt:
#     #print(code)
#     current = []
#     for word in code:
#         if 
        
        # for i in range(len(numbers)):
        #     if numbers[i] == Counter(word):
        #         print(word)
        #         print(numbers[i] == Counter(word))
        #         print(numbers[i], Counter(word))
        #         current.append(str(i))
         
                




