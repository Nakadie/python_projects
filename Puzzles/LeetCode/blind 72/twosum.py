class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    answer.append(i)
        print(answer)
        return answer

Solution().twoSum([3,3], 6), #[0,1]
Solution().twoSum([3,2,4], 6) #[1,2]

# [3,2,4]
# 6