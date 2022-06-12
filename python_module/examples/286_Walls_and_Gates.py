import collections
import math
from functools import lru_cache
from typing import List


class Solution:
    """
        You are given an m x n grid rooms initialized with these three possible values.

        -1 A wall or an obstacle.
        0 A gate.
        INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

        Example 1:

        Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
        Example 2:

        Input: rooms = [[-1]]
        Output: [[-1]]

        Constraints:

        m == rooms.length
        n == rooms[i].length
        1 <= m, n <= 250
        rooms[i][j] is -1, 0, or 231 - 1.
    """
    def wallsAndGates1(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        do not pass the all test cases
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @lru_cache(None)
        def calPath(x: int, y: int, tx: int, ty: int) -> int:
            if x == tx and y == ty:
                return 0

            if x < 0 or x > len(rooms) or y < 0 or y < len(rooms[0]) or rooms[x][y] == -1:
                return math.inf

            minPath = math.inf
            for dx, dy in directions:
                minPath = min(minPath, calPath(x + dx, y + dy, tx, ty))

            return minPath + 1

        row, col = len(rooms), len(rooms[0])
        def updatePathes(tx: int, ty: int):
            for i in range(row):
                for j in range(col):
                    if rooms[i][j] != 0 and rooms[i][j] != -1:
                        rooms[i][j] = min(rooms[i][j], calPath(i, j, tx, ty))

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    updatePathes(i, j)

    def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        """
        TTL
        :param rooms:
        :return:
        """
        if not len(rooms):
            return
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(rooms), len(rooms[0])

        def calDistance(x: int, y: int) -> int:
            """
            calculate the minimal distance to a gate
            :param x:
            :param y:
            :return:
            """
            dis = [[0] * col for _ in range(row)]
            q = collections.deque()
            q.append((x, y))
            while q:
                cx, cy = q.popleft()
                for dx, dy in directions:
                    nx = cx + dx
                    ny = cy + dy
                    if nx < 0 or nx >= row or ny < 0 or ny >= col or rooms[nx][ny] == -1 or dis[nx][ny] != 0:
                        continue

                    dis[nx][ny] = dis[cx][cy] + 1
                    if rooms[nx][ny] == 0:
                        return dis[nx][ny]
                    q.append((nx, ny))
            return 2**31 - 1

        for x in range(row):
            for y in range(col):
                if rooms[x][y] != 0 and rooms[x][y] != -1:
                    rooms[x][y] = calDistance(x, y)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not len(rooms):
            return
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(rooms), len(rooms[0])
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if cx < 0 or cx >= row or cy < 0 or cy >= col or rooms[cx][cy] == -1 or rooms[cx][cy] == 0 or rooms[cx][cy] != 2**31 - 1:
                    continue
                rooms[cx][cy] = rooms[x][y] + 1
                q.append((cx, cy))