class Solution:
    def sortArrayByParityII(self, numlist):
        sorted_ = []
        while len(numlist) > 0:
            if len(sorted_)%2 == 0:
                for i in numlist:
                    if i%2 == 0:
                        sorted_.append(i)
                        numlist.remove(i)
                        break
            else:
                for i in numlist:
                    if i%2 == 1:
                        sorted_.append(i)
                        numlist.remove(i)
                        break
       
        return sorted_