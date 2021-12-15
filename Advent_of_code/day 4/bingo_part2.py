import collections
import numpy as np
txt = open('D:\python_projects\Advent_of_code\day 4\puzzle.txt', 'r')
txt = txt.read().splitlines()
boardlist = open('D:\python_projects\Advent_of_code\day 4\jest2.txt', 'r')
boardlist = boardlist.read().splitlines()
#drawn_nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
drawn_nums = [ 22, 13, 17, 11,  0, 8,  2, 23,  4, 24, 7, 5, 19]


# drawn_nums = [txt[0]]
# drawn_nums = drawn_nums[0].split(',')
# drawn_nums = [int(x) for x in drawn_nums]
# drawn_nums = [92, 3, 88, 13, 50]


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
winners = []
def draw_and_update(drawn_nums, boards):
    boards = np.array(boards)
    possible_bingo = [
                    np.array([
                    [-1, -2, -2, -2, -2],
                    [-1, -2, -2, -2, -2],
                    [-1, -2, -2, -2, -2],
                    [-1, -2, -2, -2, -2],
                    [-1, -2, -2, -2, -2],
                ]),
                np.array([
                    [-2, -1, -2, -2, -2],
                    [-2, -1, -2, -2, -2],
                    [-2, -1, -2, -2, -2],
                    [-2, -1, -2, -2, -2],
                    [-2, -1, -2, -2, -2],
                ]),
                np.array([
                    [-2, -2, -1, -2, -2],
                    [-2, -2, -1, -2, -2],
                    [-2, -2, -1, -2, -2],
                    [-2, -2, -1, -2, -2],
                    [-2, -2, -1, -2, -2]   
                ]),
                np.array([
                    [-2, -2, -2, -1, -2],
                    [-2, -2, -2, -1, -2],
                    [-2, -2, -2, -1, -2],
                    [-2, -2, -2, -1, -2],
                    [-2, -2, -2, -1, -2],
                ]),
                np.array([
                    [-2, -2, -2, -2, -1],
                    [-2, -2, -2, -2, -1],
                    [-2, -2, -2, -2, -1],
                    [-2, -2, -2, -2, -1],
                    [-2, -2, -2, -2, -1],
                ]),
                np.array([
                    [-1, -1, -1, -1, -1],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                ]),
                np.array([
                    [-2, -2, -2, -2, -2],
                    [-1, -1, -1, -1, -1],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                ]),
                np.array([
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-1, -1, -1, -1, -1],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                ]),
                np.array([
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-1, -1, -1, -1, -1],
                    [-2, -2, -2, -2, -2],
                ]),
                np.array([
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-2, -2, -2, -2, -2],
                    [-1, -1, -1, -1, -1],
                ])
                ]
        
    for num in drawn_nums:
        print(boards)
        print('drawn', num)
        boards = np.where(boards == num, -1, boards)

        for i in boards:

            bingo_count = 0
            for x in possible_bingo:
                
                check = (i == x)
                
                occurrences = np.count_nonzero(check == True) 
                
                if occurrences == 5:
                    bingo_count += 1
                    winners.append(i)
                    print('number of winner boards = ', len(winners))
                    print(winners)
                    boards = np.where(boards > -2, -3, i)
                    
                
 

                
                
boards = get_boards()


draw_and_update(drawn_nums, boards)










