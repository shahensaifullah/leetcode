from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for index, i in enumerate(nums):
            arr.insert(index, i)
            arr.insert(index+len(nums), i)
        return arr


sol = Solution()
sol.getConcatenation([1,2,1])