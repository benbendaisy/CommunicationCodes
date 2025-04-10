from typing import List


class Solution:
    """
        You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

        A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

        Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

        Example 1:

        Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
        Output: 3
        Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
        Example 2:

        Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
        Output: 0
        Explanation: All 1s are either on the boundary or can reach the boundary.

    """
    def numEnclaves1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return
            grid[row][col] = 0
            for row_x, col_y in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
                dfs(row_x, col_y)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row == 0 or row == m - 1 or col == 0 or col == n - 1):
                    dfs(row, col)

        return sum(sum(row) for row in grid)
    
    def numEnclaves2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def helper(row: int, col: int):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return
            grid[row][col] = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                helper(new_row, new_col)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    helper(r, c)
        return sum(sum(row) for row in grid)
    
    def numEnclaves3(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def helper(row: int, col: int):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return
            
            grid[row][col] = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                helper(new_row, new_col)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row == 0 or row == m - 1 or col == 0 or col == n - 1):
                    helper(row, col)
        return sum([sum(row) for row in grid])