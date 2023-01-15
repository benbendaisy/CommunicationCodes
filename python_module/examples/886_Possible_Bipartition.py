from collections import deque
from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[yset] < self.rank[xset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
class Solution:
    """
        We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

        Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

        Example 1:

        Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
        Output: true
        Explanation: group1 [1,4] and group2 [2,3].
        Example 2:

        Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
        Output: false
        Example 3:

        Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        Output: false
    """
    def possibleBipartition2(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        dsu = UnionFind(n + 1)
        for node in range(1, n + 1):
            for neighbor in adj[node]:
                if dsu.find(node) == dsu.find(neighbor):
                    return False
                dsu.union_set(adj[node][0], neighbor)
        return True
    def possibleBipartition1(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue.
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in adj[node]:
                if color[neighbor] == node_color:
                    return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False
            return True

        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 0):
                    # Return false, if there is conflict in the component.
                    return False
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        color = [-1] * (n + 1)
        def bfs(source):
            que = deque([source])
            color[source] = 0
            while que:
                node = que.popleft()
                for neighbor in adj[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        que.append(neighbor)
            return True
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True



