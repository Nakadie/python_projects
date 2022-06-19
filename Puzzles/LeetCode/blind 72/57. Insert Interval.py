class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        buffer = []
        new_ints = []
        low = 0
        for i in intervals:
            if i[0] < newInterval[0] and i[1] > newInterval[0]:
                buffer.append(i[0])
                low = i[0]
                for j in intervals:
                    if j[0] < newInterval[1] < j[1]:
                        buffer.append(newInterval[1])
                        
            elif low == 0:
                buffer.append(i[0])
                buffer.append(i[1])
            
            # elif low > 1 and i[0] > newInterval[1]:
            #     buffer.append(i[0])
            #     buffer.append(i[1])

        print(buffer)
Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
Solution().insert([[1,3],[6,9]], [2, 5])
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]