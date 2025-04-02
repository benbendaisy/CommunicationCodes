from typing import List


class Solution:
    """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

        Example 1:

        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
        Example 2:

        Input: n = 1
        Output: [["Q"]]

        Constraints:

        1 <= n <= 9
    """
    def solveNQueens1(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        res = []
        def checkBoard(columns: list, row: int, col: int):
            for i in range(row):
                if columns[i] == col or abs(i - row) == abs(columns[i] - col):
                    return False
            return True
        def solveQueens(idx: int, columns: list):
            if idx == len(columns):
                board = [['.'] * n for _ in range(n)]
                for i in range(n):
                    board[i][columns[i]] = 'Q'
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                columns[idx] = i
                if checkBoard(columns, idx, i):
                    solveQueens(idx + 1, columns)

        columns = [0] * n
        solveQueens(0, columns)
        return res
    
    def solveNQueens2(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        
        res = []
        def check_board(cols: list, row: int, col: int):
            for i in range(row):
                if cols[i] == col or abs(i - row) == abs(cols[i] - col):
                    return False
            return True
        
        def helper(idx: int, cols: list):
            if idx == n:
                board = [['.'] * n for _ in range(n)]
                for i in range(n):
                    board[i][cols[i]] = 'Q'
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                cols[idx] = i
                if check_board(cols, idx, i):
                    helper(idx + 1, cols)
        
        cols = [0] * n
        helper(0, cols)
        return res


