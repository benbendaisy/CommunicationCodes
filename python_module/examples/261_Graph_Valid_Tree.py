from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: return False

        graph = defaultdict(lambda: [])

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = {0: -1}
        stack = [0]
        while stack:
            curNode = stack.pop()
            for neighbor in graph[curNode]:
                if neighbor == parent[curNode]:
                    continue

                if neighbor in parent:
                    return False
                parent[neighbor] = curNode
                stack.append(neighbor)
        return len(parent) == n

