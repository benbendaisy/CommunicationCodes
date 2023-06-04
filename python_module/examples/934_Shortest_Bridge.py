from typing import List


class Solution:
    """
    You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

    An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

    Example 1:

    Input: grid = [[0,1],[1,0]]
    Output: 1
    Example 2:

    Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
    Example 3:

    Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == 1)

        # dfs
        stack= [(i, j)]
        visited = set(stack)
        while stack:
            i, j = stack.pop()
            visited.add((i, j)) # mark as visited
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    stack.append((x, y))
                    visited.add((x, y))
        
        ans = 0
        queue = list(visited)
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.pop(0)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y] == 1:
                            return ans
                        queue.append((x, y))
                        visited.add((x, y))
            ans += 1
        return ans