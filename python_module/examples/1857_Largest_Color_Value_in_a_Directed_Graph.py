from collections import defaultdict
from typing import List


class Solution:
    """
        There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

        You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

        A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

        Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

        Example 1:

        Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
        Output: 3
        Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
        Example 2:

        Input: colors = "a", edges = [[0,0]]
        Output: -1
        Explanation: There is a cycle from 0 to 0.
    """
    def largestPathValue1(self, colors: str, edges: List[List[int]]) -> int:
        n, k = len(colors), 26
        in_degrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            in_degrees[v] += 1
        zero_in_degrees = set(i for i in range(n) if in_degrees[i] == 0)
        counts = [[0] * k for _ in range(n)]
        for i, c in enumerate(colors):
            counts[i][ord(c) - ord('a')] += 1
        max_cnt, visited = 0, 0
        while zero_in_degrees:
            u = zero_in_degrees.pop()
            visited += 1
            for v in graph[u]:
                for i in range(k):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    zero_in_degrees.add(v)
            max_cnt = max(max_cnt, max(counts[u]))
        return max_cnt if visited == n else -1

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(set)
        in_degrees = [0] * n
        for u, v in edges:
            graph[u].add(v)
            in_degrees[v] += 1
        que = [i for i in range(n) if in_degrees[i] == 0]
        #max freq of each colors over all paths ending at i
        colors_dict = {i : defaultdict(int) for i in range(n)}
        visited_cnt, ans = 0, 0
        while que:
            node = que.pop()
            colors_dict[node][colors[node]] += 1
            ans = max(ans, max(colors_dict[node].values()))
            visited_cnt += 1
            for v in graph[node]:
                for x in colors_dict[node]:
                    colors_dict[v][x] = max(colors_dict[v][x], colors_dict[node][x])
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    que.append(v)
        return ans if visited_cnt == n else -1

if __name__ == "__main__":
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    solution = Solution()
    ret = solution.largestPathValue(colors, edges)
    print(ret)

