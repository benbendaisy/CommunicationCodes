from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        directions = {(0, -1), (0, 1), (1, 0), (-1, 0)}
        @lru_cache(None)
        def longestIncreasingPathes(x: int, y: int) -> int:
            longestPath = 1
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] > matrix[x][y]:
                    longestPath = max(longestPath, 1 + longestIncreasingPathes(x1, y1))

            return longestPath
        maxLength = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                maxLength = max(maxLength, longestIncreasingPathes(x, y))
        return maxLength
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def helper(row: int, col: int):
            longest_path = 1
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] > matrix[row][col]:
                    longest_path = max(longest_path, 1 + helper(new_row, new_col))
            return longest_path
        
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, helper(i, j))
        return max_path

