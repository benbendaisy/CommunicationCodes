import collections
from collections import defaultdict
from typing import List


class Solution:
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
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

    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = defaultdict(lambda: [])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = {0: -1}
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if parent[node] == neighbor:
                    continue

                if neighbor in parent:
                    return False

                parent[neighbor] = node
                queue.append(neighbor)

        return len(parent) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = defaultdict(lambda: [])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                if not dfs(neighbor, node): return False

            return True

        return dfs(0, -1) and len(visited) == n

