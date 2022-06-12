import collections
import math
from typing import List


class Solution:
    """
        Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

        The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

        The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

        Example 1:

        Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        Output: 6
        Explanation: Given three friends living at (0,0), (0,4), and (2,2).
        The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
        So return 6.
        Example 2:

        Input: grid = [[1,1]]
        Output: 1

        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 200
        grid[i][j] is either 0 or 1.
        There will be at least two friends in the grid.
    """
    def minTotalDistance1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def search(r: int, c: int):
            visited = [[False] * n for _ in range(m)]
            totalDistance = 0
            q = collections.deque([(r, c, 0)])
            while q:
                r1, c1, d = q.popleft()
                if r1 < 0 or r1 >= m or c1 < 0 or c1 >= n or visited[r1][c1]:
                    continue
                visited[r1][c1] = True
                if grid[r1][c1] == 1:
                    totalDistance += d
                q.append((r1 - 1, c1, d + 1))
                q.append((r1 + 1, c1, d + 1))
                q.append((r1, c1 - 1, d + 1))
                q.append((r1, c1 + 1, d + 1))
            return totalDistance

        minDistance = math.inf
        for i in range(m):
            for j in range(n):
                minDistance = min(minDistance, search(i, j))

        return minDistance

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        algorithm:
            1, find all row nums that grid is 1
            2, find all col nums that grid is 1
            3, find the mid point of rows and the distance the the mid point
            4, find the mid point of cols and the distance the the mid point
            5, return the sum of row and col to the mid distance
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        rows = [r for r in range(m) for c in range(n) if grid[r][c] == 1] # first for is outer for loop so that rows are sorted
        cols = [c for c in range(n) for r in range(m) if grid[r][c] == 1] # first for loop is for colums so that cols are sorted
        midRow = rows[len(rows)//2]
        midCol = cols[len(cols)//2]

        rows = [abs(r - midRow) for r in rows]
        cols = [abs(c - midCol) for c in cols]
        return sum(rows) + sum(cols)

if __name__ == "__main__":
    grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    solution = Solution()
    ret = solution.minTotalDistance1(grid)
    print(ret)
