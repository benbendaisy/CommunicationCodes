from collections import defaultdict, deque
from typing import List


class Solution:
    """
        You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

        The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

        Return the length of the longest cycle in the graph. If no cycle exists, return -1.

        A cycle is a path that starts and ends at the same node.

        Example 1:

        Input: edges = [3,3,4,2,3]
        Output: 3
        Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
        The length of this cycle is 3, so 3 is returned.
        Example 2:

        Input: edges = [2,-1,3,1]
        Output: -1
        Explanation: There are no cycles in this graph.
    """
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = defaultdict(list)
        for u, v in enumerate(edges):
            if v == -1:
                continue
            graph[u].append(v)
            indegree[v] += 1
        queue = deque([node for node, indeg in enumerate(indegree) if indeg == 0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                edges[node] = -1
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] <= rank[py]:
                rank[py] += rank[px]
                parent[px] = py
            else:
                rank[px] += rank[py]
                rank[py] = px

        for u, v in enumerate(edges):
            if v == -1:
                continue
            union(u, v)
        mx = max(rank)
        return mx if mx != 1 else -1