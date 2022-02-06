def find_all(sum_dig, digs):
    import itertools
  
    possible = []
    for i in range(10**(digs-1),(10**(digs))):
        sum = 0
        for digit in str(i): 
            sum += int(digit)
        if sum == sum_dig:
            possible.append(i)
        else:
            pass
    if len(possible) == 0:
        return []
    else:
        final = sorted([sorted([int(i) for i in str(x)]) for x in possible])
        final = list(final for final,_ in itertools.groupby(final))
        for i in final:
            if len(i) != digs:
                final.remove(i)
        while final[0][0] == 0:
            try:
                for i in range(len(final)):
                    if final[i][0] == 0:
                        final.pop(i)
            except IndexError:
                pass
        final_nums = [int("".join([str(l) for l in lst])) for lst in final]
        low = final_nums[0]
        high = final_nums[-1]
        answer = [len(final), low, high]
                    
        
        return final_nums
    
print(find_all(10, 3))

#10, 3 : 118, 127, 136, 145, 226, 235, 244, 334
#desired output is [8, 118, 334]


#best answer on code wars.
# from itertools import combinations_with_replacement

# def find_all(sum_dig, digs):
#     combs = combinations_with_replacement(list(range(1, 10)), digs)
#     target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
#     if not target:
#         return []
#     return [len(target), int(target[0]), int(target[-1])]
