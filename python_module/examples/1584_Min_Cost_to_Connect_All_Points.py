import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        inGraph = [False] * n
        heap = [(0, 0)]
        minCost = 0
        edgeUsed = 0
        while edgeUsed < n:
            weight, currentNode = heapq.heappop(heap)
            if inGraph[currentNode]:
                continue

            inGraph[currentNode] = True
            minCost += weight
            edgeUsed += 1

            for i in range(n):
                if not inGraph[i]:
                    w = abs(points[i][0] - points[currentNode][0]) + abs(points[i][1] - points[currentNode][1])
                    heapq.heappush(heap, (w, i))

        return minCost
