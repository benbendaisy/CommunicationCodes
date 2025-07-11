import math
from typing import List


class Solution:
    """
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

    Note that edges may contain cycles.

    Example 1:

    Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    Output: 2
    Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
    The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
    Example 2:

    Input: edges = [1,2,-1], node1 = 0, node2 = 2
    Output: 2
    Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
    The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
    """
    def closestMeetingNode1(self, edges: List[int], node1: int, node2: int) -> int:
        que = [(node1, 1), (node2, 2)]
        n = len(edges)
        visited = [0] * n
        ans = math.inf
        while que:
            new_que = []
            find_ans = False
            for a, w in que:
                if visited[a] == 0:
                    if edges[a] != -1:
                        new_que.append((edges[a], w))
                    visited[a] = w
                elif visited[a] != w:
                    find_ans = True
                    ans = min(a, ans)
            if find_ans:
                return ans
            que = new_que
        return -1
    
    def closestMeetingNode2(edges, node1, node2):
        def get_distances(start):
            dist = {}
            curr = start
            d = 0
            while curr != -1 and curr not in dist:
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float('inf')
        result = -1

        for node in range(len(edges)):
            if node in dist1 and node in dist2:
                max_dist = max(dist1[node], dist2[node])
                if max_dist < min_dist or (max_dist == min_dist and node < result):
                    min_dist = max_dist
                    result = node

        return result
    
    def closestMeetingNode3(self, edges: List[int], node1: int, node2: int) -> int:
        def helper(node: int):
            """
            calculate the distance by dfs
            """
            dist, curr = {}, node
            d = 0
            while curr != -1 and curr not in dist:
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist
        
        dist1 = helper(node1)
        dist2 = helper(node2)

        min_dist = float("inf")
        res = -1
        for node in range(len(edges)):
            if node in dist1 and node in dist2:
                max_dist = max(dist1[node], dist2[node])
                if max_dist < min_dist:
                    min_dist = max_dist
                    res = node
        return res
    