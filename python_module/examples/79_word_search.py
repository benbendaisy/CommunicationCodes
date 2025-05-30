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
    def exist1(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.findWord(board, word, i, j, 0, visited):
                    return True
        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        def find_word(r, c, idx):
            if idx == len(word):
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = r + dx
                new_y = c + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == word[idx] and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    if find_word(new_x, new_y, idx + 1):
                        return True
                    visited[new_x][new_y] = False
            return False

        for r in range(m):
            for c in range(n):
                visited[r][c] = True
                if board[r][c] == word[0] and find_word(r, c, 1):
                    return True
                visited[r][c] = False
        return False
    
    def exist3(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        if rows * cols < len(word):
            return False

        def back_track(row, col, idx):
            if idx == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[idx]:
                return False
            
            # Mark as visited (modifies board temporarily)
            temp, board[row][col] = board[row][col], '#'

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = row + dx
                new_y = col + dy
                if back_track(new_x, new_y, idx + 1):
                    return True
            board[row][col] = temp    
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and back_track(i, j, 0):
                    return True

        return False
    
    def exist4(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False

        def helper(idx: int, row: int, col: int) -> bool:
            if idx == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False
            # visited.add((row, col))
            temp, board[row][col] = board[row][col], "#"
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if helper(idx + 1, new_row, new_col):
                    return True
                    
            # visited.remove((row, col))
            board[row][col] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(0, i, j):
                    return True
        return False
    
    def exist5(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        visited, m, n = set(), len(board), len(board[0])
        if m * n < len(word):
            return False

        def helper(idx: int, row: int, col: int) -> bool:
            if idx == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx] or (row, col) in visited:
                return False
            visited.add((row, col))
            # temp, board[row][col] = board[row][col], "#"
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if helper(idx + 1, new_row, new_col):
                    return True
                    
            visited.remove((row, col))
            # board[row][col] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(0, i, j):
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