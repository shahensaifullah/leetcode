from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str):
        if str1 == str2:
            return str1
        elif str1 + str2 != str2 + str1:
            return ""
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

sol = Solution()
a = sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB")
print(a)
