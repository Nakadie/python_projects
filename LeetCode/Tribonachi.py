class Solution:
    def tribonacci(self, n):
        answer = 0
        if n == 0:
            answer +=0
            return answer
        elif n == 1:
            answer +=1
            return answer
        elif n == 2:
            answer +=1
            return answer
        else:

            for i in range(n,0,-1):
                answer += ((self.tribonacci(i - 1)) + (self.tribonacci(i - 2)) + (self.tribonacci(i - 3)))
                print(answer)
                return answer

class_instance = Solution()
print(class_instance.tribonacci(37))

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.


# best answer:
# class Solution:
    
#     def __init__(self):
#         self.func_table = dict()
        
#         # base case:
#         self.func_table[0] = 0
#         self.func_table[1] = 1
#         self.func_table[2] = 1
        
    
#     def tribonacci(self, n: int) -> int:
        
#         if n in self.func_table:
#             # qucik resonse if tribonacci(n) has been computed before
#             return self.func_table[n]
        
#         else:
#             # recusrion with memorization 
#             self.func_table[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
#             return self.func_table[n]
            
# class_instance = Solution()
# print(class_instance.tribonacci(25))