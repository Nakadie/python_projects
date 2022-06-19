class Solution:
    def insert(self, intervals: list[list[int]], new: list[int]) -> list[list[int]]:
        buffer = []
        new_ints = []
        if intervals == []:
            print([new])
            return [new]
        for i in range(len(intervals)):
            if intervals[i][0] <  new[0] and intervals[i][1] > new[0]:
                buffer.append(intervals[i][0])
                if intervals[(i+1)][0] > new[1]:
                    buffer.append(new[1])
            elif intervals[i][0] == new[1]:
                buffer.append(intervals[i][1])
            
            elif intervals[i][0] > new[0] and intervals[i][1] < new[1]:
                pass
            else:
                buffer.append(intervals[i][0])
                buffer.append(intervals[i][1])
                
        for i in range(0,len(buffer), 2):
            new_ints.append([buffer[i],buffer[(i+1)]])
        
        return new_ints
# Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# Solution().insert([[1,3],[6,9]], [2, 5])
Solution().insert([], [100, 200])
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]