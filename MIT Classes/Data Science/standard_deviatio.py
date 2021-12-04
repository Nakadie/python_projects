import numpy as np
np.mean

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    else:
        lens = []
        sums = []
        for i in L:
            lens.append(len(i))
        mean = np.mean(lens)
        for i in lens:
            sums.append((i-mean)**2)
        return np.sqrt(sum(sums)/len(L))
    





L = [10, 4, 12, 15, 20, 5]
print(stdDevOfLengths(L))