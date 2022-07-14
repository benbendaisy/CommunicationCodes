import math
from collections import deque
from typing import List


class Solution:
    """
        You are given an m x n grid grid of values 0, 1, or 2, where:

        each 0 marks an empty land that you can pass by freely,
        each 1 marks a building that you cannot pass through, and
        each 2 marks an obstacle that you cannot pass through.
        You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

        Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

        The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

        The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

        Example 1:

        Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        Output: 7
        Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
        The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
        So return 7.
        Example 2:

        Input: grid = [[1,0]]
        Output: 1
        Example 3:

        Input: grid = [[1]]
        Output: -1

        Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0, 1, or 2.
        There will be at least one building in the grid.
    """
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # 对于每一个 1(buiding),进行bfs找到它每一个empty_island的距离，然后累加跟新它到每一个empty_island的距离
        m, n = len(grid), len(grid[0])
        empty_island = 0
        dist = [[0]*(n) for _ in range(m)]


        def dfs(i, j, empty_island):
            ans = math.inf
            # 容易confuse的重点：
            # 只有更新到最后一个building, 这里的ans才是最后的ans，平时只是用来看这个building是不是至少能走到一个empty island
            # 如果一个empty island也不能走到，ans不能被跟新，最后就是math.inf。特别的，如果不能走到一个empty islands,这个grid[ni][nj]上的数字不能被减去1，下一次的更新新也不会走这个数
            # 所以最后dist中最小的数字，不一定和ans相等
            q = deque([(i, j, 0)])
            while q:
                i, j, d = q.popleft()
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == empty_island:
                        grid[ni][nj] -= 1
                        dist[ni][nj] += (d+1)
                        q.append((ni, nj, d+1))
                        ans = min(ans,dist[ni][nj]) #  只有最后一次也能走到的空地才能是最后的答案
            return ans


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = dfs(i, j, empty_island)
                    empty_island -= 1
                    if ans == math.inf:
                        return -1
        return ans

    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        The basic ideas are sumarized below:
        1, using queue to calculate the houses to all empty ilands
        2, reuse the dist to accumulate the distances that all houses come here to avoid visit the empty iland twice
        3, use emptyIland to represents empty ilands so that next house can travel here
        4, early terminate if there is no empty iland but still a house want to travel
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        emptyIland = 0 #represents the empty islands as we need to change it so that we can sum all distances

        def calculateAllDistances(i, j, emptyIland):
            """
            Calculate the distance beteen the house i, j to all empty ilands
            :param i:
            :param j:
            :param emptyIland:
            :return:
            """
            ans = math.inf
            que = deque([(i, j, 0)])
            #calculate the distance between the i, j to all empty ilands
            while que:
                i, j, d = que.popleft()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newI, newJ = i + di, j + dj
                    if 0 <= newI < m and 0 <= newJ < n and grid[newI][newJ] == emptyIland:
                        grid[newI][newJ] -= 1 # mark it as empty iland for next house
                        dist[newI][newJ] += d + 1
                        que.append((newI, newJ, d + 1))
                        ans = min(ans, dist[newI][newJ])
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = calculateAllDistances(i, j, emptyIland)
                    emptyIland -= 1
                    if ans == math.inf:
                        return -1
        return ans
