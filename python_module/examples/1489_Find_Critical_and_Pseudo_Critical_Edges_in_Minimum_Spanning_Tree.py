from typing import List

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.weight = 0
        self.edge_count = 0
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y, w):
        r1 = self.find(x)
        r2 = self.find(y)
        if r1 != r2:
            self.parents[r2] = self.parents[r1]
            self.weight += w
            self.edge_count += 1


class Solution:
    """
    Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weight] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

    Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

    Note that you can return the indices of the edges in any order.

    Example 1:

    Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    Output: [[0,1],[2,3,4,5]]
    Explanation: The figure above describes the graph.
    The following figure shows all the possible MSTs:

    Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
    The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
    Example 2:

    Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    Output: [[],[0,1,2,3]]
    Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
    """
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(w, a, b, i)  for i, (a, b, w) in enumerate(edges)]
        edges.sort()

        uf1 = UnionFind(n)
        for w, a, b, _ in edges:
            uf1.union(a, b, w)
        min_weight = uf1.weight
        ce = []
        pce = []
        m = len(edges)

        for i in range(m):
            uf2 = UnionFind(n)
            for j in range(m):
                if i == j:
                    continue
                w, a, b, _ = edges[j]
                uf2.union(a, b, w)
            if uf2.weight > min_weight or uf2.edge_count < n - 1:
                ce.append(edges[i][3])
            else:
                uf3 = UnionFind(n)
                w, a, b, _ = edges[i]
                uf3.union(a, b, w)
                for j in range(m):
                    w, a, b, _ = edges[j]
                    uf3.union(a, b, w)
                if uf3.weight == min_weight:
                    pce.append(edges[i][3])
        return ce, pce