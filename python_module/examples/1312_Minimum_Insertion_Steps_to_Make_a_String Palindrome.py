class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        s2 = s[::-1]

        dp = [[0] * (length + 1) for _ in range(length + 1)]
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                if s[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + max(dp[i - 1][j], dp[i][j - 1])

        return dp[length][length]