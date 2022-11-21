from collections import deque
from typing import List


class Solution:
    """
        You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

        Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

        Example 1:

        Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
        Output: 6
        Explanation:
        The shortest path without eliminating any obstacle is 10.
        The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
        Example 2:

        Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
        Output: -1
        Explanation: We need to eliminate at least two obstacles to find such a walk.
    """
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)

        # if we have sufficient quotas to eliminate the obstacles in the worst case,
        # then the shortest distance is the Manhattan distance
        if k >= rows + cols - 2:
            return rows + cols - 2

        # (row, col, remaining quota to eliminate obstacles)
        state = (0, 0, k)
        queue = deque([(0, state)])
        seen = set([state])

        while queue:
            steps, (row, col, m) = queue.popleft()

            # we reach the target here
            if (row, col) == target:
                return steps

            # explore the four directions in the next step
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # if (new_row, new_col) is within the grid boundaries
                newX = row + dx
                newY = col + dy
                if 0 <= newX < rows and 0 <= newY < cols:
                    newElimination = m - grid[newX][newY]
                    newState = (newX, newY, newElimination)
                    # add the next move in the queue if it qualifies
                    if newElimination >= 0 and newState not in seen:
                        seen.add(newState)
                        queue.append((steps + 1, newState))
        return -1