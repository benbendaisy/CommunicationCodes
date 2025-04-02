class Solution:
    """
        You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

        Connect: A cell is connected to adjacent cells horizontally or vertically.
        Region: To form a region connect every 'O' cell.
        Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
        To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

        Example 1:

        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

        Explanation:


        In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

        Example 2:

        Input: board = [["X"]]

        Output: [["X"]]
    """
    def solve1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def helper(row: int, col: int, symb: str):
            if board[row][col] != "O":
                return
            board[row][col] = symb
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if 0 < new_row < m - 1 and 0 < new_col < n - 1:
                    helper(new_row, new_col, symb)
        
        for c in range(n):
            if board[0][c] == "O":
                helper(0, c, "C")
            if board[m - 1][c] == "O":
                helper(m - 1, c, "C")

        for r in range(m):
            if board[r][0] == "O":
                helper(r, 0, "C")
            if board[r][n - 1] == "O":
                helper(r, n - 1, "C")
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    helper(r, c, "X")
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'C':
                    board[r][c] = 'O'


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def helper(row: int, col: int, symb: str):
            if board[row][col] != "O":
                return
            board[row][col] = symb
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if 0 < new_row < m - 1 and 0 < new_col < n - 1:
                    helper(new_row, new_col, symb)
        
        for c in range(n):
            if board[0][c] == "O":
                helper(0, c, "C")
            if board[m - 1][c] == "O":
                helper(m - 1, c, "C")

        for r in range(m):
            if board[r][0] == "O":
                helper(r, 0, "C")
            if board[r][n - 1] == "O":
                helper(r, n - 1, "C")
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
    
    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        queue = deque()
        
        # Step 1: Collect all boundary 'O' positions in the queue
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n - 1] == 'O':
                queue.append((i, n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m - 1][j] == 'O':
                queue.append((m - 1, j))

        # Step 2: Perform BFS to mark all boundary-connected 'O' cells
        while queue:
            r, c = queue.popleft()
            if board[r][c] != 'O':
                continue
            board[r][c] = 'C'
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    queue.append((nr, nc))

        # Step 3: Convert all 'O' to 'X' (captured regions), and 'C' back to 'O' (safe regions)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'C':
                    board[r][c] = 'O'
    
    def solve3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def helper(row: int, col: int, symb: str):
            if board[row][col] != "O":
                return
            board[row][col] = symb
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if 0 < new_row < m - 1 and 0 < new_col < n - 1:
                    helper(new_row, new_col, symb)
        
        for c in range(n):
            if board[0][c] == "O":
                helper(0, c, "C")
            if board[m - 1][c] == "O":
                helper(m - 1, c, "C")

        for r in range(m):
            if board[r][0] == "O":
                helper(r, 0, "C")
            if board[r][n - 1] == "O":
                helper(r, n - 1, "C")
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'C':
                    board[r][c] = 'O'