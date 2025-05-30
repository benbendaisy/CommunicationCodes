from functools import lru_cache


class Solution:
    """
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

        The test cases are generated so that the answer will be less than or equal to 2 * 109.

        Example 1:

        Input: m = 3, n = 7
        Output: 28
        Example 2:

        Input: m = 3, n = 2
        Output: 3
        Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down

        Constraints:

        1 <= m, n <= 100
    """
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        @lru_cache(None)
        def paths(r, c):
            if r == m - 1 or c == n - 1:
                return 1
            elif r < 0 or r >= m or c < 0 or c >= n:
                return 0

            return paths(r, c + 1) + paths(r + 1, c)

        return paths(0, 0)
    

    def uniquePaths3(self, m: int, n: int) -> int:
        
        @cache
        def helper(row: int, col: int):
            if row == m - 1 and col == n - 1:
                return 1
            
            if row >= m or row < 0 or col >= n or col < 0:
                return 0
            
            return helper(row + 1, col) + helper(row, col + 1)

        return helper(0, 0)
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        mod = 2 * 10 ** 9
        @cache
        def helper(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1:
                return 1
            if row == m or col == n:
                return 0
            
            return helper(row + 1, col) + helper(row, col + 1)

        return helper(0, 0) %  mod

