import heapq
import math
from typing import List


class Solution:
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        row, col = len(heights), len(heights[0])

        self.max_so_far = math.inf
        visited = [[False] * col for _ in range(row)]
        @lru_cache(None)
        def dfs(x, y, max_diff):
            if x == row - 1 and y == col - 1:
                self.max_so_far = min(self.max_so_far, max_diff)
                return max_diff

            min_effort = math.inf
            visited[x][y] = True
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                adjx, adjy = x + dx, y + dy

                # check adjacent cell and make sure we do not visited before
                if 0 <= adjx < row and 0<= adjy < col and not visited[adjx][adjy]:
                    # compare the max_diff with current diff
                    current_diff = abs(heights[adjx][adjy] - heights[x][y])
                    max_current_diff = max(max_diff, current_diff)
                    # only need to go further if max_current_diff is small than max_so_far
                    # otherwise, max_so_far (solution) is better than current solution
                    if max_current_diff < self.max_so_far:
                        res = dfs(adjx, adjy, max_current_diff)
                        min_effort = min(min_effort, res)

            visited[x][y] = False
            return min_effort

        return dfs(0, 0, 0)

    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        """
        dijiskara
        :param heights:
        :return:
        """
        if not heights:
            return 0
        row, col = len(heights), len(heights[0])
        heap =[(0, 0, 0)]
        visited = [[False] * col for _ in range(row)]
        max_diffs = [[math.inf] * col for _ in range(row)]
        max_diffs[0][0] = 0
        while heap:
            _, x, y = heapq.heappop(heap)
            visited[x][y] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0<= new_x < row and 0<= new_y < col and not visited[new_x][new_y]:
                    cur_diff = abs(heights[new_x][new_y] - heights[x][y])
                    max_diff = max(cur_diff, max_diffs[x][y])
                    if max_diff < max_diffs[new_x][new_y]:
                        max_diffs[new_x][new_y] = max_diff
                        heapq.heappush(heap, (max_diff, new_x, new_y))
        return max_diffs[-1][-1]

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = [x for x in range(size)]
                self.rank = [0] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                parentX, parentY = self.find(x), self.find(y)

                if parentX != parentY:
                    if self.rank[parentX] < self.rank[parentY]:
                        parentX, parentY = parentY, parentX
                    self.parent[parentY] = parentX
                    if self.rank[parentX] == self.rank[parentY]:
                        self.rank[parentX] += 1

        row, col = len(heights), len(heights[0])
        if row == 1 and col == 1:
            return 0

        edges = []
        for cur_row in range(row):
            for cur_col in range(col):
                if cur_row > 0:
                    diff = abs(heights[cur_row][cur_col] - heights[cur_row - 1][cur_col])
                    edges.append((diff, cur_row * col + cur_col, (cur_row - 1) * col + cur_col))
                if cur_col > 0:
                    diff = abs(heights[cur_row][cur_col] - heights[cur_row][cur_col - 1])
                    edges.append((diff, cur_row * col + cur_col, cur_row * col + cur_col - 1))

        edges.sort()
        unionFind = UnionFind(row * col)
        for diff, x, y in edges:
            unionFind.union(x, y)
            if unionFind.find(0) == unionFind.find(row * col - 1):
                return diff
        return -1