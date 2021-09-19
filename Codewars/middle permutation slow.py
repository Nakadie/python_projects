# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:14:28 2021

@author: Kamuela
"""

from itertools import permutations


def middle_permutation(string):
    final = sorted([''.join(each) for each in permutations(string)])
    if len(final)%2 == 0:
       return final[int(len(final)/2 -1)]
       
    else:
       return final[int(len(final)/2)]
    
  
print(middle_permutation('abcdxg'))
#expected output
# ("abc"),"bac") works
# ("abcd"),"bdca") works
# ("abcdx"),"cbxda") works
# ("abcdxg"),"cxgdba") works
# ("abcdxgz"),"dczxgba") too slow cant return
    

# ("abc"),"bac") works
# ("abcd"),"bdca") works
# ("abcdx"),"cbxda") works
# ("abcdgx"),"cxgdba") works
# ("abcdgxz"),"dczxgba") too slow cant return

123 = 213
1234 = 2431
12345 = 32541
123456 = 365421
1234567 = 4376521