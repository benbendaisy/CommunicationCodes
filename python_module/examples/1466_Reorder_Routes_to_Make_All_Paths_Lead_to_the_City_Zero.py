from collections import deque, defaultdict
from typing import List


class Solution:
    """
        There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

        Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

        This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

        Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

        It's guaranteed that each city can reach city 0 after reorder.

        Example 1:

        Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        Output: 3
        Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
        Example 2:

        Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
        Output: 2
        Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
        Example 3:

        Input: n = 3, connections = [[1,0],[2,0]]
        Output: 0
    """
    def minReorder1(self, n: int, connections: List[List[int]]) -> int:
        "TLE"
        city_dict = {0}
        cnt = 0
        queue = deque(connections)
        while queue:
            u, v = queue.popleft()
            if v in city_dict:
                city_dict.add(u)
            elif u in city_dict:
                city_dict.add(v)
                cnt += 1
            else:
                queue.append([u, v])
        return cnt

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add((b, True))
            graph[b].add((a, False))
        # reverse the path from 0 to any node
        queue = deque([(0, False)])
        ans = 0
        visited = set()
        while queue:
            city, need_flip = queue.popleft()
            visited.add(city)
            if need_flip:
                ans += 1
            for neighbour in graph[city]:
                if neighbour[0] not in visited:
                    queue.append(neighbour)
        return ans