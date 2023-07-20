from typing import List


class Solution:
    """
    Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

    Example 1:

    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.
    Example 2:

    Input: grid = [[3,2],[1,0]]
    Output: 0
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        row, col = rows - 1, 0
        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                cnt += cols - col
                row -= 1
            else:
                col += 1
        return cnt