class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        dp = [[0 for x in range(len(s) + 1)] for y in range(len(t) + 1)]
        for j in range(len(dp[0])):
            dp[0][j] = j

        for i in range(len(dp)):
            dp[i][0] = i

        for i in range(len(dp) + 1):
            for j in range(len(dp[0]) + 1):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1
                    if dp[i + 1][j + 1] > i + j + 1:
                        return False

        return True

