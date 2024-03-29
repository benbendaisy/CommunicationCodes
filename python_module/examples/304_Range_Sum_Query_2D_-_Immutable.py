from functools import lru_cache
from typing import List


class NumMatrix:
    """
        Given a 2D matrix matrix, handle multiple queries of the following type:

        Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
        Implement the NumMatrix class:

        NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
        int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

        Example 1:

        Input
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
        Output
        [null, 8, 11, 12]

        Explanation
        NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
        numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
        numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
        numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

        Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 200
        -105 <= matrix[i][j] <= 105
        0 <= row1 <= row2 < m
        0 <= col1 <= col2 < n
        At most 104 calls will be made to sumRegion.
    """

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        r, c = len(matrix), len(matrix[0])
        self.dp = [[0] * (c + 1) for _ in range(r)]
        for i in range(r):
            for j in range(c):
                self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        for r in range(row1, row2 + 1):
            sums += self.dp[r][col2 + 1] - self.dp[r][col1]
        return sums

    def sumRegion1(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cnt = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                cnt += self.matrix[i][j]
        return cnt