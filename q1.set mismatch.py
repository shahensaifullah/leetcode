from http.cookiejar import cut_port_re
from typing import List
from icecream import ic

class Solution:
    def findErrorNums(self, nums: List[int]):
        h = {}
        ans = [0] * 2

        for num in nums:
            if num in h:
                h[num] +=1
            else:
                h[num] = 1

        for i in h:
            if h[i] == 2:
                ans[0] = i

        for i in range(1,len(nums)+1):
            if i not in h:
                ans[1] = i
        return ans


sol = Solution()
print(sol.findErrorNums(nums = [1,2,2,4])) # [2,3] 1-4=-3
print(sol.findErrorNums(nums = [2,2])) # [2,1]
print(sol.findErrorNums(nums = [3,2,2])) # [2,1] 3-2 = 1
# ic("=====================")
# ic(sol.findErrorNums(nums = [2,2,1])) # [2,1]

