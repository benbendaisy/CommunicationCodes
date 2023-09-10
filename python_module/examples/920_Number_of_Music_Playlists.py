class Solution:
    def numMusicPlaylists1(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dfs(i, x):
            if i == goal:
                return x == n
            ans = 0
            if x < n:
                ans += (n - x) * dfs(i + 1, x + 1)
            if k < x:
                ans += (x - k) * dfs(i + 1, x)
            return ans % mod
        return dfs(0, 0)
    
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j - 1] * (n - (j - 1))) % mod
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod
        return dp[goal][n]