import collections
import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    """
        You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
        We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

        Example 1:
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
        Example 2:

        Input: times = [[1,2,1]], n = 2, k = 1
        Output: 1
        Example 3:

        Input: times = [[1,2,1]], n = 2, k = 2
        Output: -1

        Constraints:

        1 <= k <= n <= 100
        1 <= times.length <= 6000
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        0 <= wi <= 100
        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
    """
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1

        def calculateWeights(node, visited):
            if not node or parent[node][0][0] == -1 or node in visited:
                return 0
            visited.add(node)
            return parent[node][0][1] + calculateWeights(parent[node][0][0], visited)

        graph = defaultdict(lambda: [])
        for source, target, weight in times:
            graph[source].append((target, weight))

        queue = collections.deque([k])
        parent = defaultdict(lambda: [])
        parent[k].append((-1, -1))
        visited = set()
        while queue:
            node = queue.popleft()
            if graph[node] and not node in visited:
                for target, weight in graph[node]:
                    parent[target].append((node, weight))
                    queue.append(target)
            visited.add(node)

        if len(parent) < n:
            return -1

        maxWeights = 0
        for node in range(1, n + 1):
            visited = set()
            maxWeights = max(maxWeights, calculateWeights(node, visited))

        return maxWeights

    def networkDelayTime(self, times, n, k):
        pq, visited, graph = [(0, k)], {}, collections.defaultdict(lambda: [])
        for u, v, w in times:
            graph[u].append((v, w))
        while pq:
            time, node = heapq.heappop(pq)
            if node not in visited:
                visited[node] = time
                for v, w in graph[node]:
                    heapq.heappush(pq, (time + w, v))
        return max(visited.values()) if len(visited) == n else -1

if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    solution = Solution()
    ret = solution.networkDelayTime(times, 4, 2)
    print(ret)

