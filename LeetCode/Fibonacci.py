class Solution:
    def fib(self, n):
        fibo = 0
        if n == 0:
            fibo +=0
            return fibo
        elif n == 1:
            fibo +=1
            return fibo
        else:

            for i in range(n,0,-1):
                fibo += ((self.fib(i - 1)) + (self.fib(i - 2)))

                return fibo

class_instance = Solution()
print(class_instance.fib(5))
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.











# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.