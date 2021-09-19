# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:03:35 2021

@author: Kamuela
"""

# array = [[1,2,3,4],
#          [5,6,7,8],
#          [9,10,11,12],
#          [13,14,15,16]
#          ]
array = [[456, 810, 456, 426, 500, 654, 867, 597, 791, 756, 269, 802, 932, 980, 363],
         [818, 578, 335, 343, 391, 818, 376, 260, 994, 459, 636, 895, 582, 39, 922],
         [144, 897, 536, 885, 642, 862, 559, 731, 826, 939, 958, 695, 603, 830, 780],
         [497, 65, 440, 250, 295, 422, 142, 785, 695, 89, 744, 226, 102, 333, 721],
         [691, 927, 957, 279, 623, 407, 78, 829, 107, 16, 311, 810, 198, 703, 149],
         [189, 864, 405, 726, 11, 962, 448, 597, 816, 42, 218, 244, 441, 634, 819], 
         [412, 77, 674, 780, 857, 867, 15, 153, 82, 585, 250, 141, 74, 212, 461], 
         [125, 867, 14, 661, 962, 903, 737, 113, 74, 642, 542, 985, 253, 567, 407], 
         [609, 599, 648, 838, 764, 792, 739, 202, 45, 530, 766, 932, 852, 807, 635], 
         [899, 675, 165, 161, 143, 713, 258, 570, 77, 63, 962, 55, 390, 91, 165], 
         [814, 286, 575, 596, 924, 247, 603, 297, 993, 516, 75, 597, 689, 219, 364], 
         [827, 187, 881, 950, 903, 68, 41, 505, 222, 257, 621, 559, 445, 670, 664], 
         [767, 505, 776, 343, 690, 690, 39, 539, 975, 817, 633, 65, 877, 23, 824], 
         [642, 440, 351, 413, 744, 360, 590, 695, 233, 258, 589, 284, 993, 282, 543], 
         [183, 668, 80, 121, 469, 148, 872, 825, 568, 533, 837, 437, 148, 622, 905]]


def snail(array):
    path = []
    #wait untill the array is empty if empty finished.
    while bool(array) == True:
        row =[]
        col = []
        prepath = []
        try: #if there is an index error the list is possibly empty so break the loop to check if it is empty
    #appends the top of the list going to the right
            for i in array[0]: 
                row.append(i)
    # appends furthest right number going down.
            for i in range(len(array[0])-1):
                col.append(array[i+1][-1]) 
        
            array.pop(0) #removes iterated list
            prepath = row + col 
            path += prepath #records the path
    #removes farthest right variable     
            for i in range(len(array[0])- 1):
                array[i].pop(len(array))
    # counts the bottom row in reverse         
            for i in reversed(array[-1]):
                path.append(i)
            array.pop(-1)#removes bottom row.
      # counts first integer in rows going bottom to top     
            for i in reversed(range(len(array))):
                path.append(array[i][0]) 
      # removes the counted numbers.         
            for i in range(len(array[0])-1):
                array[i].pop(0) 
        except IndexError:
            pass

    return path
    
    
    
print(snail(array))
        