from typing import List

from icecream import ic

'''
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies
'''


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candides = max(candies)
        results = []

        for candy in candies:
            if candy + extraCandies >= max_candides:
                results.append(True)
            else:
                results.append(False)
        return results


sol = Solution()
# a = sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
a = sol.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1)
print(a)