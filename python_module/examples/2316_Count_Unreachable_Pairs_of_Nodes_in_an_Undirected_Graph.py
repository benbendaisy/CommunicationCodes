from typing import List


class Solution:
    """
        You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

        Return the number of pairs of different nodes that are unreachable from each other.

        Example 1:

        Input: n = 3, edges = [[0,1],[0,2],[1,2]]
        Output: 0
        Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
        Example 2:

        Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
        Output: 14
        Explanation: There are 14 pairs of nodes that are unreachable from each other:
        [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
        Therefore, we return 14.
    """
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        root = list(range(n)) # Initialize the root of each vertex as itself
        size = [1] * n # Initialize the size of each group as 1
        groups = {*range(n)} # Initialize the root of each vertex as itself
        def union(x: int, y: int):
            def find(x: int):
                if x != root[x]: # if x is not root, keep tracing the root
                    root[x] = find(root[x]) # Path compression
                    x = root[x] # trace root
                return x # Root found
            px, py = find(x), find(y) # Find the roots of x and y
            if px != py: # Different roots means there are not in same group
                # Merge smaller group into bigger group. => Weighted Quick Union
                if size[px] > size[py]:
                    size[px] += size[py]
                    root[py] = root[px]
                    groups.discard(py)  # smaller group root removed after union
                else:
                    size[py] += size[px]
                    root[px] = root[py]
                    groups.discard(px)
        for a, b in edges:
            union(a, b)
        pairs = 0
        for node in groups: # Traverse roots of groups
            n -= size[node] # Number of the total size of non-visited groups
            pairs += n * size[node] # Add the pairs between group r and non-visited groups
        return pairs

