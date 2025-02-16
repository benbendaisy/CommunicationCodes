from typing import List


class Solution:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    Example 2:

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        def traverse_visit(r1, c1, r2, c2):
            if r2 < r1 or c2 < c1:
                return
            for i in range(c1, c2 + 1):
                res.append(matrix[r1][i])
            # handle the last row    
            if r1 == r2:
                return
            for i in range(r1 + 1, r2 + 1):
                res.append(matrix[i][c2])
            # handle the last column
            if c1 == c2:
                return
            for i in range(c2 - 1, c1 - 1, -1):
                res.append(matrix[r2][i])
            for i in range(r2 - 1, r1, -1):
                res.append(matrix[i][c1])
            traverse_visit(r1 + 1, c1 + 1, r2 - 1, c2 - 1)
        traverse_visit(0, 0, m - 1, n - 1)
        return res
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        down, up, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            for i in range(left, right + 1):
                res.append(matrix[down][i])
            down += 1
            if down > up:
                break
            for i in range(down, up + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[up][i])
            up -= 1
            if up < down:
                break
            for i in range(up, down - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res