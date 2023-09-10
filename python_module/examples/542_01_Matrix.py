from typing import List


class Solution:
    """
    Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

    The distance between two adjacent cells is 1.

    Example 1:

    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
    Example 2:

    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        que = deque()
        max_value = m * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                else:
                    mat[i][j] = max_value
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while que:
            x, y = que.popleft()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0<= new_y < n and mat[new_x][new_y] > mat[x][y] + 1:
                    que.append((new_x, new_y))
                    mat[new_x][new_y] = mat[x][y] + 1
        return mat 