import itertools
def next_smaller(n):
    strver = str(n)
    digits = []
    x = 0
    for i in strver:
        digits.append(i)
    
    for num in int(itertools.permutations(''.join(digits))):
        
        print(num)
        if num < n and num > x:
            x = num
    print(num)
   
    
    # if len(possible) == 0:
    #     return -1
    # else:
    #     return possible[-1]
    

print(next_smaller(907))



# test.assert_equals(next_smaller(907), 790)
# test.assert_equals(next_smaller(531), 513)
# test.assert_equals(next_smaller(135), -1)
# test.assert_equals(next_smaller(2071), 2017)
# test.assert_equals(next_smaller(414), 144)
# test.assert_equals(next_smaller(123456798), 123456789)
# test.assert_equals(next_smaller(123456789), -1)
# test.assert_equals(next_smaller(1234567908), 1234567890)