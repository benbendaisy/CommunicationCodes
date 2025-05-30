from typing import List


class Solution:
    """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1
        Example 2:

        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3


        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.
    """
    def numIslands1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != "1":
                return
            grid[row][col] = "-1"
            for dx, dy in directions:
                dfs(row + dx, col + dy)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt

    def numIslands2(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        def blood_search(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                x = row + dx
                y = col + dy
                blood_search(x, y)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    cnt += 1
                    blood_search(r, c)
        return cnt
    
    def numIslands3(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        def helper(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
                return
            grid[row][col] = "2"
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                new_row = row + dx
                new_col = col + dy
                helper(new_row, new_col)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt += 1
                    helper(i, j)
        return cnt
    
    def numIslands4(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def helper(row: int, col: int):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                return
            grid[row][col] = '0'
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                helper(new_row, new_col)
        
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    helper(r, c)
                    cnt += 1
        return cnt
    
    def numIslands5(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def helper(row: int, col: int):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != "1":
                return
            grid[row][col] = "2"
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                helper(new_row, new_col)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    helper(i, j)
        return cnt

