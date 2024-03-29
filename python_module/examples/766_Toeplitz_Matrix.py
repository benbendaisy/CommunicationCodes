from typing import List


class Solution:
    """
        Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

        Example 1:

        Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        Output: true
        Explanation:
        In the above grid, the diagonals are:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
        In each diagonal all elements are the same, so the answer is True.
        Example 2:

        Input: matrix = [[1,2],[2,2]]
        Output: false
        Explanation:
        The diagonal "[1, 2]" has different elements.

        Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 20
        0 <= matrix[i][j] <= 99
    """
    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        groups = {}
        for r in range(m):
            for c in range(n):
                if (r - c) not in groups:
                    groups[r - c] = matrix[r][c]
                elif groups[r - c] != matrix[r][c]:
                    return False
        return True
