from typing import List
from functools import lru_cache

class Solution:
    """
    You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

    An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

    Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

    The testcases are generated so that the answer will be less than or equal to 2 * 109.

    Example 1:

    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
    Example 2:

    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

    Constraints:

    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
    """
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @lru_cache(None)
        def uniquePaths(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n or obstacleGrid[x][y] == 1:
                return 0
            elif x == m - 1 and y == n - 1:
                return 1

            return uniquePaths(x + 1, y) + uniquePaths(x, y + 1)

        return uniquePaths(0, 0)

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] ==  1:
            return 0

        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]
    
    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:
        mod = 2 * 10 ** 9
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def helper(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1:
                if obstacleGrid[row][col] == 1:
                    return 0 
                return 1
            
            if row == m or col == n:
                return 0
            
            if obstacleGrid[row][col] == 1:
                return 0
            
            return helper(row + 1, col) + helper(row, col + 1)
        
        return helper(0, 0)
    
    def uniquePathsWithObstacles4(self, obstacleGrid: List[List[int]]) -> int:
        mod = 2 * 10 ** 9
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def helper(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1 and obstacleGrid[row][col] != 1:
                return 1
            if row == m or col == n:
                return 0
            
            if obstacleGrid[row][col] == 1:
                return 0
            
            return (helper(row + 1, col) + helper(row, col + 1)) % mod
        
        return helper(0, 0)

if __name__ == "__main__":
    solution = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

    ret = solution.uniquePathsWithObstacles(obstacleGrid)
    print(ret)