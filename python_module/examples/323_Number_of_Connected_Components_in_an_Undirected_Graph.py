from collections import defaultdict
from typing import List

class DJS:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {x:x for x in vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item

        return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

class Solution:
    """
        You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

        Return the number of connected components in the graph.

        Example 1:

        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2
        Example 2:

        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1

        Constraints:

        1 <= n <= 2000
        1 <= edges.length <= 5000
        edges[i].length == 2
        0 <= ai <= bi < n
        ai != bi
        There are no repeated edges.
    """
    def countComponents1(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for nextNode in graph[node]:
                dfs(nextNode)

        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DJS([x for x in range(n)])
        for edge in edges:
            ds.union(edge[0], edge[1])
        parent = set()
        for i in range(n):
            parent.add(ds.find(i))
        return len(parent)