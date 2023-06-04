import collections
from typing import List


class Solution:
    """
        Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

        A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

        All the visited cells of the path are 0.
        All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
        The length of a clear path is the number of visited cells of this path.

        Example 1:

        Input: grid = [[0,1],[1,0]]
        Output: 2
        Example 2:

        Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
        Output: 4
        Example 3:

        Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
        Output: -1

        Constraints:

        n == grid.length
        n == grid[i].length
        1 <= n <= 100
        grid[i][j] is 0 or 1
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        row, col = len(grid) - 1, len(grid[0]) - 1
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        def getNeighbors(r: int, c: int):
            for idx, idy in directions:
                xrow, ycol = r + idx, c + idy
                if not (0 <= xrow <= row and 0 <= ycol <= col):
                    continue
                elif grid[xrow][ycol] != 0:
                    continue
                yield (xrow, ycol)

        if grid[0][0] == 1 or grid[row][col] == -1:
            return -1
        queue = collections.deque([(0, 0)])
        grid[0][0] = 1
        while queue:
            curRow, curCol = queue.popleft()
            distance = grid[curRow][curCol]
            if curRow == row and curCol == col:
                return distance
            for nextRow, nextCol in getNeighbors(curRow, curCol):
                grid[nextRow][nextCol] = distance + 1
                queue.append((nextRow, nextCol))

        return -1