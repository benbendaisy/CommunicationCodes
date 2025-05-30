from typing import List


class Solution:
    """
        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        Example 1:

        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
        Example 2:

        Input: grid = [[1,2,3],[4,5,6]]
        Output: 12
    """
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
    
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[-1][-1]
    
    def minPathSum3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def helper(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            if row == m or col == n:
                return float('inf')
            
            return grid[row][col] + min(helper(row + 1, col), helper(row, col + 1))
        
        return helper(0, 0)
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def helper(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            elif row == m or col == n:
                return float('inf')

            return min(helper(row + 1, col), helper(row, col + 1)) + grid[row][col]
        res = helper(0, 0)
        return -1 if res == float('inf') else res
