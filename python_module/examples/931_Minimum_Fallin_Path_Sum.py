import math
from functools import lru_cache
from typing import List


class Solution:
    """
        Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

        A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

        Example 1:

        Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
        Output: 13
        Explanation: There are two falling paths with a minimum sum as shown.
        Example 2:

        Input: matrix = [[-19,57],[-40,-5]]
        Output: -59
        Explanation: The falling path with a minimum sum is shown.
    """
    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        @lru_cache(None)
        def min_falling_path_sum(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return math.inf

            if r == rows - 1:
                return matrix[r][c]

            left = min_falling_path_sum(r + 1, c - 1)
            middle = min_falling_path_sum(r + 1, c)
            right = min_falling_path_sum(r + 1, c + 1)

            return min(left, middle, right) + matrix[r][c]

        min_falling_sum = math.inf
        for c in range(cols):
            min_falling_sum = min(min_falling_sum, min_falling_path_sum(0, c))
        return min_falling_sum

    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n):
                if c == 0:
                    dp[r][c] = min(dp[r + 1][c], dp[r + 1][c + 1]) + matrix[r][c]
                elif c == n - 1:
                    dp[r][c] = min(dp[r + 1][c], dp[r + 1][c - 1]) + matrix[r][c]
                else:
                    dp[r][c] = min(dp[r + 1][c - 1], dp[r + 1][c], dp[r + 1][c + 1]) + matrix[r][c]

        min_path_sum = math.inf
        for c in range(n):
            min_path_sum = min(min_path_sum, dp[0][c])
        return min_path_sum

    def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        @cache
        def falling_path_sum(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return math.inf
            if r == rows - 1:
                return matrix[r][c]
            left =  falling_path_sum(r + 1, c - 1)
            middle = falling_path_sum(r + 1, c)
            right = falling_path_sum(r + 1, c + 1)
            return min(left, middle, right) + matrix[r][c]
        min_sum = math.inf
        for c in range(cols):
            min_sum = min(min_sum, falling_path_sum(0, c))
        return min_sum
    
    def minFallingPathSum4(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @cache
        def helper(row: int, col: int) -> int:
            if row == rows - 1:
                if 0 <= col < cols:
                    return matrix[row][col]
                return float('inf')
            if col < 0 or col >= cols:
                return float('inf')

            return min(helper(row + 1, col - 1), helper(row + 1, col), helper(row + 1, col + 1)) + matrix[row][col]
        
        min_sum = float('inf')
        for col in range(cols):
            min_sum = min(min_sum, helper(0, col))
        return min_sum
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0:
                    dp[row][col] = matrix[row][col]
                elif col == 0:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col + 1]) + matrix[row][col]
                elif col == cols - 1:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1]) + matrix[row][col]
                else:
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1]) + matrix[row][col]
        return min(dp[-1])