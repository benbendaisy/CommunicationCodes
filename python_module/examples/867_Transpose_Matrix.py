from typing import List


class Solution:
    """
        Given a 2D integer array matrix, return the transpose of matrix.

        The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

        Example 1:

        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[1,4,7],[2,5,8],[3,6,9]]
        Example 2:

        Input: matrix = [[1,2,3],[4,5,6]]
        Output: [[1,4],[2,5],[3,6]]

        Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 1000
        1 <= m * n <= 105
        -109 <= matrix[i][j] <= 109
    """
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        newMatrix = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                newMatrix[j][i] = matrix[i][j]

        return newMatrix
