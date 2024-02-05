from typing import List


class Solution:
    """
    Given an m x n binary matrix mat, return the number of special positions in mat.

    A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

    Example 1:

    Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
    Output: 1
    Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
    Example 2:

    Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
    """
    def numSpecial1(self, mat: List[List[int]]) -> int:
        res = 0
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    continue
                good = True
                for r in range(m):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                if good:
                    for c in range(n):
                        if c != col and mat[row][c] == 1:
                            good = False
                            break
                if good:
                    res += 1
        return res
    
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_cnt, col_cnt = [0] * m, [0] * n
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_cnt[row] += 1
                    col_cnt[col] += 1
        res = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_cnt[row] == 1 and col_cnt[col] == 1:
                        res += 1
        return res