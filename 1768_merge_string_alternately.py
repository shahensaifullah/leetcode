class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_words = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged_words.append(word1[i])

            if i < len(word2):
                merged_words.append(word2[i])

        return "".join(merged_words)



sol = Solution()
sol.mergeAlternately(word1 = "abc", word2 = "pqrqq")