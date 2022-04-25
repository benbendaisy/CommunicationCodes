class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        length1, length2 = len(text1), len(text2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(length1 + 1):
            for j in range(length2 + 1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0

        return dp[length1][length2]

    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        def longestCommonSub(str1: str, str2: str, idx1: int, idx2: int):
            if idx1 >= len(str1) or idx2 >= len(str2):
                return 0

            maxLength = 0
            if str1[idx1] == str2[idx2]:
                maxLength = max(maxLength, longestCommonSub(str1, str2, idx1 + 1, idx2 + 1))

            maxLength = max(maxLength, max(longestCommonSub(str1, str2, idx1 + 1, idx2), longestCommonSub(str1, str2, idx1, idx2 + 1)))

            return maxLength

        return longestCommonSub(text1, text2, 0, 0)