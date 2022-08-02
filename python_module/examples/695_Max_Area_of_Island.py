from typing import List


class Solution:
    """
        You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

        The area of an island is the number of cells with a value 1 in the island.

        Return the maximum area of an island in grid. If there is no island, return 0.

        Example 1:

        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6
        Explanation: The answer is not 11, because the island must be connected 4-directionally.
        Example 2:

        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0

        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0 or 1.
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def calculateAreaOfIsland(row: int, col: int):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            area = 1
            grid[row][col] = 0
            for idx, idy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rowx = row + idx
                coly = col + idy
                area += calculateAreaOfIsland(rowx, coly)
            return area

        r, c = len(grid), len(grid[0])
        maxArea = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, calculateAreaOfIsland(i, j))

        return maxArea

