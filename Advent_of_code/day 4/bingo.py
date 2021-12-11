import collections
import numpy as np
from numpy.core.records import array
txt = open('D:\python_projects\Advent_of_code\day 4\puzzle.txt', 'r')
txt = txt.read().splitlines()
boardlist = open('D:\python_projects\Advent_of_code\day 4\puzzle2.txt', 'r')
boardlist = boardlist.read().splitlines()

drawn_nums = [txt[0]]
drawn_nums = drawn_nums[0].split(',')
drawn_nums = [int(x) for x in drawn_nums]
#drawn_nums = [92, 3, 88, 13, 50]


def get_boards():
    temp = [x for x in boardlist if x != '']
    boards = []
    board = []
    for i in temp:
        if len(board) != 5:
            board.append([int(k) for k in i.split()])
        if len(board) == 5:
            boards.append(board)
            board = []
    return boards

def draw_and_update(drawn_nums):
    y = 0
    boards = np.array(get_boards(), dtype=object)
    for num in drawn_nums:
        boards = np.where(boards == num, 'x', boards)
        if check_bingo(boards) == True:
            print(num)
            break
        
                
                
                
def check_bingo(boards):
    possible_bingo = [
                np.array([
                ['x', '', '', '', ''],
                ['x', '', '', '', ''],
                ['x', '', '', '', ''],
                ['x', '', '', '', ''],
                ['x', '', '', '', ''],
            ]),
            np.array([
                ['', 'x', '', '', ''],
                ['', 'x', '', '', ''],
                ['', 'x', '', '', ''],
                ['', 'x', '', '', ''],
                ['', 'x', '', '', ''],
            ]),
            np.array([
                ['', '', 'x', '', ''],
                ['', '', 'x', '', ''],
                ['', '', 'x', '', ''],
                ['', '', 'x', '', ''],
                ['', '', 'x', '', ''],
            ]),
            np.array([
                ['', '', '', 'x', ''],
                ['', '', '', 'x', ''],
                ['', '', '', 'x', ''],
                ['', '', '', 'x', ''],
                ['', '', '', 'x', ''],
            ]),
            np.array([
                ['', '', '', '', 'x'],
                ['', '', '', '', 'x'],
                ['', '', '', '', 'x'],
                ['', '', '', '', 'x'],
                ['', '', '', '', 'x'],
            ]),
            np.array([
                ['x', 'x', 'x', 'x', 'x'],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
            ]),
            np.array([
                ['', '', '', '', ''],
                ['x', 'x', 'x', 'x', 'x'],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
            ]),
            np.array([
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['x', 'x', 'x', 'x', 'x'],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
            ]),
            np.array([
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['x', 'x', 'x', 'x', 'x'],
                ['', '', '', '', ''],
            ]),
            np.array([
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['x', 'x', 'x', 'x', 'x'],
            ])
            ]
    boards = np.array(boards)
    for i in boards:
        for x in possible_bingo:
            check = (i == x)
            occurrences = np.count_nonzero(check == True)
            if occurrences == 5:
                final = np.sum(np.where(i == 'x', 0, i))
                print(final)
                return True
                
    
            
           


boards = get_boards()

draw_and_update(drawn_nums)


