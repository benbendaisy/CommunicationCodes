from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
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
if __name__ == "__main__":
    arr = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution = Solution()
    ret = solution.gameOfLife(arr)
    print(arr)