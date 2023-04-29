from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        dp = [0] * length

        for i in range(length - 2, -1, -1):
            prev = 0
            for j in range(i + 1, length):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                prev = temp
        return dp[length - 1]

    def minInsertions1(self, s: str) -> int:
        @lru_cache(None)
        def dfs(left, right):
            if left >= right:
                return 0

            if s[left] == s[right]:
                return dfs(left + 1, right - 1)

            return min(dfs(left + 1, right), dfs(left, right - 1)) + 1
        return dfs(0, len(s) - 1)
