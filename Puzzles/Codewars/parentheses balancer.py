# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:22:04 2021

@author: Kamuela
"""
from itertools import combinations, combinations_with_replacement, permutations
def balanced_parens(n):
    last = []
    parens = '12' * n
    if n == 0:
        return ''
    final = [i for i in permutations(parens, n*2)]
    
    final = [list(i) for i in final if i[0] != '2' and i[-1] != '1']
    # final = list(set(final))
    
    
    for i in range(len(final)):
        try:
            
            for x in range(len(final[i])):
                y = 0
                if final[i][x] == '2':
                    final.pop(i)
                else:    
                    while final[i][x] == '1':
                        if final[i][y] == '2':
                            final[i][x] = ('(')
                            final[i][y] = (')')
                            x+=1
                        else:
                            y += 1
        except IndexError:
            pass
    
        
                
    # final = [i for i in final if i !=]
    final = [''.join(w) for w in final]
    final = list(set(final))
    
    return print(final)
    
    
        
    
        


balanced_parens(4)



                   #  [ [0, [""]],
                   # [1, ["()"]],
                   # [2, ["(())","()()"]],
                   # [3, ["((()))","(()())","(())()","()(())","()()()"]]
                   # [4, ['(()()())', '()(()())', '(()())()', '(())(())', '((())())', '()((()))', '()(())()', '()()(())', '(()(()))', '(())()()', '((()))()', '()()()()', '((()()))', '(((())))']
                   
                    
                       
                       # 12
                       # 1122, 1212
                       # 111222, 112122,112212,121122,121212
                       # 11112222, 11121222, 11122122, 
                       
                       
Best answer
def balanced_parens(n):
    '''
    To construct all the possible strings with n pairs of balanced parentheses 
    this function makes use of a stack of items with the following structure:
        (current, left, right)
    Where:
        current is the string being constructed
        left is the count of '(' remaining
        right is the count of  ')' remaining
    '''
    stack = [('', n, 0)]
    result = []
    
    # Loop until we run out of items in the stack
    while stack:
        current, left, right = stack.pop()
        
        # if no '(' or ')' left to add, add current to the result
        if left == 0 and right == 0:
            result.append(current)
            
        # if we can, add a '(' and return to the stack
        if left > 0:
            stack.append((current + '(', left - 1, right + 1))
            
        # if we can, add a ')' and return to the stack    
        if right > 0:
            stack.append((current + ')', left, right - 1))
            
    return result