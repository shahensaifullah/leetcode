from typing import List
from icecream import ic

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev= nums[0] # 1
        count_1 = 0
        max_count = 0
        for i in nums: #
            if i == 1: #
                if i == prev: # 1
                    count_1+=1 #
                else:
                    count_1 = 1
            else:
                if count_1 > max_count:
                    max_count = count_1
                count_1 = 0
            prev = i

        return max_count if max_count > count_1 else count_1





sol = Solution()
print(sol.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print("====================")
print(sol.findMaxConsecutiveOnes(nums = [0,0]))
print(sol.findMaxConsecutiveOnes(nums = [1,1,1]))
