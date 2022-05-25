from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = {(0, -1), (0, 1), (1, 0), (-1, 0)}
        @lru_cache(None)
        def longestIncreasingPathes(x: int, y: int) -> int:
            longestPath = 1
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] < matrix[x][y]:
                    longestPath = max(longestPath, 1 + longestIncreasingPathes(x1, y1))

            return longestPath
        maxLength = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                maxLength = max(maxLength, longestIncreasingPathes(x, y))
        return maxLength

