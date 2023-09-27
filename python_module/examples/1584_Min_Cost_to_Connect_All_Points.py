import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        in_graph = [False] * n
        heap = [(0, 0)]
        min_cost = 0
        edge_used = 0
        while edge_used < n:
            weight, node = heapq.heappop(heap)
            if in_graph[node]:
                continue
            in_graph[node] = True
            min_cost += weight
            edge_used += 1
            for i in range(n):
                if not in_graph[i]:
                    w = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                    heapq.heappush(heap, (w, i))
        return min_cost
