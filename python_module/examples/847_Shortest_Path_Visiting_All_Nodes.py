from typing import List


class Solution:
    """
    You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

    Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

    Example 1:

    Input: graph = [[1,2,3],[0],[0],[0]]
    Output: 4
    Explanation: One possible path is [1,0,2,0,3]
    Example 2:

    Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    Output: 4
    Explanation: One possible path is [0,1,4,2,3]
    """
    def shortestPathLength1(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        que = []
        visited = set()
        for node, _ in enumerate(graph):
            state = 1 << node
            que.append((0, node, state))
            visited.add((node, state))
        target = (1 << n) - 1

        while que:
            dis, node, state = deque.heappop(que)
            for nei in graph[node]:
                nei_state = 1 << nei | state
                if nei_state == target:
                    return dis + 1
                if (nei, nei_state) in visited:
                    continue
                deque.heappush(que, (dis + 1, nei, nei_state))
                visited.add((nei, nei_state))
    
    def shortestPathLength2(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final_mask = (1 << n) - 1

        que = deque([[i, 1 << i, 0] for i in range(n)])
        visited = set((i, i << i) for i in range(n))
        while que:
            node, mask, steps = que.popleft()
            if mask == final_mask:
                return steps
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    que.append([neighbor, new_mask, steps + 1])
        return -1
    
    def shortestPathLength3(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_mask = (1 << n) - 1
        que = deque([i, 1 << i, 0] for i in range(n))
        visited = set((i, 1 << i) for i in range(n))

        while que:
            node, mask, steps = que.popleft()
            if mask == all_mask:
                return steps
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    que.append([neighbor, new_mask, steps + 1])
        return -1
    
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_mask = (1 << n) - 1
        que = deque([i, 1 << i, 0] for i in range(n))
        visited = set((i, 1 << i) for i in range(n))
        while que:
            node, mask, steps = que.popleft()
            if mask == all_mask:
                return steps

            for neighbor in graph[node]:
                new_mask = mask | 1 << neighbor
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    que.append((neighbor, new_mask, steps + 1))
        return -1
    
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph:
            return 0
        n = len(graph)
        mask_all = (1 << n) - 1
        que = deque([(i, 1 << i, 0) for i in range(n)])
        visited = set((i, 1 << i) for i in range(n))

        while que:
            node, mask, steps = que.popleft()
            if mask == mask_all:
                return steps

            for nxt in graph[node]:
                new_mask = mask | (1 << nxt)
                if (nxt, new_mask) not in visited:
                    visited.add((nxt, new_mask))
                    que.append((nxt, new_mask, steps + 1))     
        return -1

