class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = [1] * m
        cols = [1] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        
        for i in range(m):
            if rows[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if cols[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

        You must do it in place.

        Example 1:

        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]
        Example 2:

        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(m):
                matrix[i][j] = 0