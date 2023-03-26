from typing import List


class Solution:
    """
        There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

        You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

        Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

        Example 1:

        Input: n = 4, connections = [[0,1],[0,2],[1,2]]
        Output: 1
        Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
        Example 2:

        Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
        Output: 2
        Example 3:

        Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
        Output: -1
        Explanation: There are not enough cables.
    """
    def makeConnected1(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        graph = [set() for _ in range(n)]
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        visited = [0] * n
        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1
        return sum(dfs(node) for node in range(n)) - 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n -1:
            return -1

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x == parent_y:
                return
            if rank[parent_x] > rank[parent_y]:
                parent[parent_y] = parent_x
                rank[parent_x] += rank[parent_y]
            else:
                parent[parent_x] = parent_y
                rank[parent_y] += rank[parent_x]

        unconnected = n - 1
        for u, v in connections:
            if find(u) == find(v):
                continue
            unconnected -= 1
            union(u, v)
        return unconnected