from typing import List


class Solution:
    """
        Alice and Bob have an undirected graph of n nodes and three types of edges:

        Type 1: Can be traversed by Alice only.
        Type 2: Can be traversed by Bob only.
        Type 3: Can be traversed by both Alice and Bob.
        Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

        Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

        Example 1:

        Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
        Output: 2
        Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
        Example 2:

        Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
        Output: 0
        Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
        Example 3:

        Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
        Output: -1
        Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

    """
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i, root):
            if i != root[i]:
                root[i] = find(root[i], root)
            return root[i]

        def union(x, y, root):
            x, y = find(x, root), find(y, root)
            if x == y:
                return 0
            root[x] = y
            return 1

        res = alice_edges = bob_edges = 0

        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if union(i, j, root):
                    alice_edges += 1
                    bob_edges += 1
                else:
                    res += 1
        root0 = root[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j, root):
                    alice_edges += 1
                else:
                    res += 1

        root = root0
        for t, i, j in edges:
            if t == 2:
                if union(i, j , root):
                    bob_edges += 1
                else:
                    res += 1

        return res if alice_edges == bob_edges == n - 1 else -1




