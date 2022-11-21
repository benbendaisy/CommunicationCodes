from collections import deque
from typing import List


class Solution:
    """
        You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

        In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

        Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

        Example 1:

        Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
        Output: 1
        Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
        Initially, you are at the entrance cell [1,2].
        - You can reach [1,0] by moving 2 steps left.
        - You can reach [0,2] by moving 1 step up.
        It is impossible to reach [2,3] from the entrance.
        Thus, the nearest exit is [0,2], which is 1 step away.
        Example 2:

        Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
        Output: 2
        Explanation: There is 1 exit in this maze at [1,2].
        [1,0] does not count as an exit since it is the entrance cell.
        Initially, you are at the entrance cell [1,0].
        - You can reach [1,2] by moving 2 steps right.
        Thus, the nearest exit is [1,2], which is 2 steps away.
        Example 3:

        Input: maze = [[".","+"]], entrance = [0,0]
        Output: -1
        Explanation: There are no exits in this maze.
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        # Mark the entrance as visited since its not a exit.
        st_row, st_col = entrance
        maze[st_row][st_col] = "+"
        # Start BFS from the entrance, and use a queue `queue` to store all
        # the cells to be visited.
        queue = deque([(st_row, st_col, 0)])
        while queue:
            row, col, step = queue.popleft()
            # For the current cell, check its four neighbor cells.
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + dx
                new_col = col + dy
                # If there exists an unvisited empty neighbor:
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == ".":
                    # If this empty cell is an exit, return distance + 1.
                    if new_row == 0 or new_row == m - 1 or new_col == 0 or new_col == n - 1:
                        return step + 1
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, step + 1))
        # If we finish iterating without finding an exit, return -1.
        return -1
