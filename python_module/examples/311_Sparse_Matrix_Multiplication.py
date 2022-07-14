from typing import List


class Solution:
    """
        Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

        Example 1:

        Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
        Output: [[7,0,0],[-7,0,3]]
        Example 2:

        Input: mat1 = [[0]], mat2 = [[0]]
        Output: [[0]]

        Constraints:

        m == mat1.length
        k == mat1[i].length == mat2.length
        n == mat2[i].length
        1 <= m, n, k <= 100
        -100 <= mat1[i][j], mat2[i][j] <= 100
    """
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def getColumns(rows: int, col: int):
            arr = []
            for row in range(rows):
                arr.append(mat2[row][col])
            return arr

        def innerProduct(arr1:List[int], arr2:List[int]):
            sums = 0
            for a, b in zip(arr1, arr2):
                sums += a * b
            return sums

        matrix = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                col = getColumns(len(mat2), j)
                matrix[i][j] = innerProduct(mat1[i], col)
        return matrix

