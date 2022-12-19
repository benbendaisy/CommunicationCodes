from functools import lru_cache


class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        length1 = len(text1)
        length2 = len(text2)

        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[length1][length2]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        def longestCommonSub(str1: str, str2: str, idx1: int, idx2: int):
            if idx1 >= len(str1) or idx2 >= len(str2):
                return 0

            if str1[idx1] == str2[idx2]:
                return 1 + longestCommonSub(str1, str2, idx1 + 1, idx2 + 1)
            else:
                return max(longestCommonSub(str1, str2, idx1 + 1, idx2), longestCommonSub(str1, str2, idx1, idx2 + 1))

        return longestCommonSub(text1, text2, 0, 0)


    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def longest_common_subsequence(idx1: int, idx2: int):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + longest_common_subsequence(idx1 + 1, idx2 + 1)

            return max(longest_common_subsequence(idx1 + 1, idx2), longest_common_subsequence(idx1, idx2 + 1))
        return longest_common_subsequence(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]