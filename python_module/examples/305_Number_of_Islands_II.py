from typing import List
class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = {i:i for i in range(n)}
            self.size = {i:1 for i in range(n)}

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            parentX = self.find(x)
            parentY = self.find(y)
            if parentX == parentY:
                return

            if self.size[parentX] <= self.size[parentY]:
                self.parent[parentX] = parentY
                self.size[parentY] += self.size[parentX]
            else:
                self.parent[parentY] = parentX
                self.size[parentX] += self.size[parentY]

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = self.UnionFind(m * n)
        res = []
        cnt = 0
        visited = set() # to hold all islands
        for x, y in positions:
            if (x, y) in visited:
                res.append(cnt)
                continue

            cnt += 1
            visited.add((x, y))
            # connecting the islands
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextX, nextY = x + dx, y + dy
                if nextX < 0 or nextX >= m or nextY < 0 or nextY >= n or (nextX, nextY) not in visited: # skip if nextX, nextY is not an island
                    continue

                parentOld, parentNew = uf.find(x * n + y), uf.find(nextX * n + nextY)
                if parentOld != parentNew:
                    uf.union(parentNew, parentOld)
                    cnt -= 1
            res.append(cnt)
        return res



class Solution1:
    """
        You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

        We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

        Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

        Example 1:

        Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
        Output: [1,1,2,3]
        Explanation:
        Initially, the 2d grid is filled with water.
        - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
        - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
        - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
        - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
        Example 2:

        Input: m = 1, n = 1, positions = [[0,0]]
        Output: [1]

        Constraints:

        1 <= m, n, positions.length <= 104
        1 <= m * n <= 104
        positions[i].length == 2
        0 <= ri < m
        0 <= ci < n
    """
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r:int, c:int, visited:List[List[bool]]):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or visited[r][c]:
                return
            visited[r][c] = True

            for dx, dy in directions:
                dfs(r + dx, c + dy, visited)

        def countIsland():
            visited = [[False] * n for _ in range(m)]
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        dfs(i, j, visited)
                        cnt += 1
            return cnt

        res = []
        for px, py in positions:
            grid[px][py] = 1
            res.append(countIsland())
        return res

