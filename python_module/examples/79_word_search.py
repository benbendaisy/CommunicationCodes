from typing import List


class Solution:
    def findWord(self, board: List[List[str]], word: str, row: int, col: int, idx: int, visited: List[List[bool]]) -> bool:
        if idx == len(word):
            return True
        elif col < 0 or col >= len(board[0]) or row < 0 or row >= len(board) \
                or visited[row][col] or board[row][col] != word[idx]:
            return False
        visited[row][col] = True
        idx += 1
        discovered = self.findWord(board, word, row - 1, col, idx, visited) \
                     or self.findWord(board, word, row + 1, col, idx, visited) \
                     or self.findWord(board, word, row, col - 1, idx, visited) \
                     or self.findWord(board, word, row, col + 1, idx, visited)

        visited[row][col] = False
        return discovered
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.findWord(board, word, i, j, 0, visited):
                    return True
        return False

if __name__ == "__main__":
    solution = Solution()
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"
    ret = solution.exist(board, word)
    print(ret)