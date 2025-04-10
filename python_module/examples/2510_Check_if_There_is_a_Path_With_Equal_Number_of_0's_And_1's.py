class Solution:
    """
    You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1).

    Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.


    Example 1:


    Input: grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
    Output: true
    Explanation: The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.
    Example 2:


    Input: grid = [[1,1,0],[0,0,1],[1,0,0]]
    Output: false
    Explanation: There is no path in this grid with an equal number of 0's and 1's.
    """
    def isThereAPath1(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        @cache
        def helper(row, col, balance):
            if grid[row][col] == 0:
                balance += 1
            else:
                balance -= 1
            if row == m - 1 and col == n - 1:
                return balance == 0
            elif row < m - 1 and helper(row + 1, col, balance):
                return True
            elif col < n - 1 and helper(row, col + 1, balance):
                return True
            return False
        return helper(0, 0, 0)
    
    def isThereAPath2(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        @cache
        def helper(row: int, col: int, balance: int) -> bool:
            if row >= m or col >= n:
                return False

            if grid[row][col] == 1:
                balance += 1
            elif grid[row][col] == 0:
                balance -= 1

            if row == m - 1 and col == n - 1:
                return balance == 0

            for dx, dy in ((1, 0), (0, 1)):
                new_r, new_c = row + dx, col + dy
                if helper(new_r, new_c, balance):
                    return True
            return False
        return helper(0, 0, 0)
    
    def isThereAPath3(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True
        
        m, n = len(grid), len(grid[0])
        @cache
        def helper(row: int, col: int, balance: int) -> bool:
            if row >= m or col >= n:
                return False
            balance += -1 if grid[row][col] == 0 else 1
            if row == m - 1 and col == n - 1:
                return balance == 0
            for dx, dy in ((1, 0), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if helper(new_row, new_col, balance):
                    return True
                    
            return False
        
        return helper(0, 0, 0)
    
    def isThereAPath4(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True
        
        m, n = len(grid), len(grid[0])
        @cache
        def helper(row: int, col: int, balance: int) -> bool:
            if row == m - 1 and col == n - 1:
                return balance == 0

            for dx, dy in ((1, 0), (0, 1)):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_balance = balance + (-1 if grid[new_row][new_col] == 0 else 1)
                    if helper(new_row, new_col, new_balance):
                        return True
            return False
        balance = -1 if grid[0][0] == 0 else 1
        return helper(0, 0, balance)
