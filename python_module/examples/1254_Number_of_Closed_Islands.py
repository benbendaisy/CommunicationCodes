from typing import List


class Solution:
    """
        Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

        Return the number of closed islands.

        Example 1:

        Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        Output: 2
        Explanation:
        Islands in gray are closed because they are completely surrounded by water (group of 1s).
        Example 2:

        Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        Output: 1
        Example 3:

        Input: grid = [[1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,1,0,1,0,1],
                       [1,0,1,1,1,0,1],
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        Output: 2
    """
    def closedIsland1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        @lru_cache(None)
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            if grid[row][col] == 1:
                return True
            grid[row][col] = 1
            return dfs(row, col - 1) and dfs(row, col + 1) and dfs(row - 1, col) and dfs(row + 1, col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and dfs(i, j):
                    cnt += 1
        return cnt
    
    def closedIsland2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def helper(row: int, col: int) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if grid[row][col] == 1:
                return True
            grid[row][col] = 1

            return all(helper(row + dx, col + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)))

        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and helper(r, c):
                    cnt += 1
        return cnt
    
    def closedIsland3(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        @cache
        def helper(row: int, col: int) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            
            if grid[row][col] == 1:
                return True
            
            grid[row][col] = 1
            
            if all(helper(row + dx, col + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))):
                return True
            return False
        cnt = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and helper(row, col):
                    cnt += 1
        return cnt