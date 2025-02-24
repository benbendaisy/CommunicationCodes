from functools import lru_cache


class Solution:
    """
        There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

        Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

        Example 1:

        Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
        Output: 6
        Example 2:

        Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
        Output: 12

        Constraints:

        1 <= m, n <= 50
        0 <= maxMove <= 50
        0 <= startRow < m
        0 <= startColumn < n
    """
    def findPaths1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def calculatePaths(rowx: int, colx: int, curMove: int):
            if rowx < 0 or rowx >= m or colx < 0 or colx >= n:
                return 1
            elif curMove == 0:
                return 0

            curPath = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newX = rowx + dx
                newY = colx + dy
                curPath += calculatePaths(newX, newY, curMove - 1)
            return curPath % ((10**9)+7)

        return calculatePaths(startRow, startColumn, maxMove)
    
    def findPaths2(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def calculate_path(row, col, cur_move):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            elif cur_move == 0:
                return 0
            cur_path = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = row + dx
                y = col + dy
                cur_path += calculate_path(x, y, cur_move - 1)
            return cur_path % ((10**9)+7)
        return calculate_path(startRow, startColumn, maxMove)
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def helper(row: int, col: int, move: int):
            if move > maxMove:
                return 0
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            
            path = 0
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row = row + dx
                new_col = col + dy
                path += helper(new_row, new_col, move + 1)

            return path      
        return helper(startRow, startColumn, 0) % mod