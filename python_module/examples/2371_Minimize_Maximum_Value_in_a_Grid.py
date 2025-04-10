class Solution:
    """
    You are given an m x n integer matrix grid containing distinct positive integers.

    You have to replace each integer in the matrix with a positive integer satisfying the following conditions:

    The relative order of every two elements that are in the same row or column should stay the same after the replacements.
    The maximum number in the matrix after the replacements should be as small as possible.
    The relative order stays the same if for all pairs of elements in the original matrix such that grid[r1][c1] > grid[r2][c2] where either r1 == r2 or c1 == c2, then it must be true that grid[r1][c1] > grid[r2][c2] after the replacements.

    For example, if grid = [[2, 4, 5], [7, 3, 9]] then a good replacement could be either grid = [[1, 2, 3], [2, 1, 4]] or grid = [[1, 2, 3], [3, 1, 4]].

    Return the resulting matrix. If there are multiple answers, return any of them.

    Example 1:

    Input: grid = [[3,1],[2,5]]
    Output: [[2,1],[1,2]]
    Explanation: The above diagram shows a valid replacement.
    The maximum number in the matrix is 2. It can be shown that no smaller value can be obtained.
    Example 2:

    Input: grid = [[10]]
    Output: [[1]]
    Explanation: We replace the only number in the matrix with 1.
    """
    def minScore1(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row, col = [0] * m, [0] * n
        heapify(heap:= [(grid[i][j], i, j) for i, j in product(range(m), range(n))])
        while heap:
            _, i, j = heappop(heap)
            grid[i][j] = row[i] = col[j] = max(row[i], col[j]) + 1
        return grid

    def minScore2(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row, col = [0] * m, [0] * n
        arr = sorted(product(range(m), range(n)), key = lambda x: grid[x[0]][x[1]])
        for i, j in arr:
            grid[i][j] = row[i] = col[j] = max(row[i], col[j]) + 1
        return grid
    
    def minScore3(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        min_heap = []
        rows = [1] * m
        cols = [1] * n

        for i in range(m):
            for j in range(n):
                heapq.heappush(min_heap, (grid[i][j], i, j))
        
        while min_heap:
            _, i, j = heapq.heappop(min_heap)
            val = max(rows[i], cols[j])
            grid[i][j] = val
            rows[i] = cols[j] = val + 1
        return grid
    
    def minScore4(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid:
            return []
        m, n = len(grid), len(grid[0])
        min_heap = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(min_heap, (grid[i][j], i, j))
        
        rows, cols = [1] * m, [1] * n
        while min_heap:
            _, row, col = heapq.heappop(min_heap)
            val = max(rows[row], cols[col])
            grid[row][col] = val
            rows[row] = cols[col] = val + 1
        return grid