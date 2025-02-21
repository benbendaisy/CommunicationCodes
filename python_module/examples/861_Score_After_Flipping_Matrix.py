class Solution:
    """
    You are given an m x n binary matrix grid.

    A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

    Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

    Return the highest possible score after making any number of moves (including zero moves).

    Example 1:

    Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Output: 39
    Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
    Example 2:

    Input: grid = [[0]]
    Output: 1
    """
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def toggle_row(row: int):
            for j in range(cols):
                grid[row][j] = 1 - grid[row][j]
        def toggle_col(col: int):
            for i in range(rows):
                grid[i][col] = 1 - grid[i][col]
        def convert(arry: List[int]):
            res = 0
            for v in arry:
                res = res * 2 + v
            return res
        
        
        for i in range(rows):
            if grid[i][0] == 0:
                toggle_row(i)

        for j in range(cols):
            cnt = 0
            column = [row[j] for row in grid]
            for c in column:
                if c == 1:
                    cnt += 1
            if cnt <= rows // 2:
                toggle_col(j)

        res = 0
        for row in grid:
            res += convert(row)
        return res