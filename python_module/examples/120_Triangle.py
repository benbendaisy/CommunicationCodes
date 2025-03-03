import math
from functools import lru_cache
from typing import List


class Solution:
    """
        Given a triangle array, return the minimum path sum from top to bottom.

        For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


        Example 1:

        Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        Output: 11
        Explanation: The triangle looks like:
           2
          3 4
         6 5 7
        4 1 8 3
        The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
        Example 2:

        Input: triangle = [[-10]]
        Output: -10

        Constraints:

        1 <= triangle.length <= 200
        triangle[0].length == 1
        triangle[i].length == triangle[i - 1].length + 1
        -104 <= triangle[i][j] <= 104

        Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
    """
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        m = len(triangle)
        @lru_cache(None)
        def minTotals(row: int, col: int):
            if row == m:
                return 0
            return triangle[row][col] + min(minTotals(row + 1, col), minTotals(row + 1, col + 1))

        return minTotals(0, 0)

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        @cache
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path
        return min_path(0, 0)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        @cache
        def helper(row: int, col: int):
            if row == rows:
                return 0
            return triangle[row][col] + min(helper(row + 1, col), helper(row + 1, col + 1))

        return helper(0, 0)

if __name__ == "__main__":
    triangle = [[-1],[2,3],[1,-1,-3]]
    solution = Solution()
    ret = solution.minimumTotal(triangle)
    print(ret)