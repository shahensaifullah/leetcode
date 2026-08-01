# https://leetcode.com/problems/maximum-length-of-pair-chain/
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]):
        pairs.sort(key=lambda x: x[1])

        prev = 0
        count = 1
        for i in range(1, len(pairs)):
            if pairs[prev][1] < pairs[i][0]:
                prev = i
                count+=1

        return count









sol = Solution()
print(sol.findLongestChain(pairs = [[1,2],[2,3],[3,4]]))
print(sol.findLongestChain(pairs = [[1,2],[7,8],[4,5]]))