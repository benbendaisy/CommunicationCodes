from typing import List


class Solution:
    def gameOfLife1(self, board: List[List[int]]) -> None:
        """
        According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

        The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

        Given the current state of the board, update the board to reflect its next state.

        Note that you do not need to return anything.
        
        Example 1:

        Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        Example 2:

        Input: board = [[1,1],[1,0]]
        Output: [[1,1],[1,1]]
        """
        rows, cols = len(board), len(board[0])
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        copiedBoard = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                liveCount = 0
                for neighbor in neighbors:
                    r, c = row + neighbor[0], col + neighbor[1]
                    if ((r >= 0 and r < rows) and (c >= 0 and c < cols)) and copiedBoard[r][c] == 1:
                        liveCount += 1
                if copiedBoard[row][col] == 1 and (liveCount < 2 or liveCount > 3):
                    board[row][col] = 0
                elif copiedBoard[row][col] == 0 and liveCount == 3:
                    board[row][col] = 1
    

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)}
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                lives = 0
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy
                    if 0 <= new_row < m and 0 <= new_col < n and abs(board[new_row][new_col]) == 1:
                        lives += 1
                if board[row][col] == 1 and (lives < 2 or lives > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2

        for row in range(m):
            for col in range(n):
                if board[row][col] == -1:
                    board[row][col] = 0
                if board[row][col] == 2:
                    board[row][col] = 1


if __name__ == "__main__":
    arr = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution = Solution()
    ret = solution.gameOfLife(arr)
    print(arr)