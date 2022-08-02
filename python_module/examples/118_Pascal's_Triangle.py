from typing import List


class Solution:
    """
        Given an integer numRows, return the first numRows of Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

        Example 1:

        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        Example 2:

        Input: numRows = 1
        Output: [[1]]
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for r in range(numRows):
            row = [None for _ in range(r + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j]
            triangle.append(row)
        return triangle