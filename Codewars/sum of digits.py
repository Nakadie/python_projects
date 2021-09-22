def find_all(sum_dig, digs):
  
    final_list = []
    digs = digs
    sum_dig = sum_dig
    while len(final_list) < digs - 2:
        for i in range(1,10):
            if (sum_dig - i) >= 0:
                final_list.append(i)
                sum_dig -= i
                i += 1
            else:
                pass
    return final_list

print(find_all(10, 3))
