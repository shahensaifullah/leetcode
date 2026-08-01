from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_arr = []
        for i in range(0,n):
            new_arr.append(nums[i])
            new_arr.append(nums[i+n])
        return new_arr




sol = Solution()
print(sol.shuffle(nums = [2,5,1,3,4,7], n = 3))