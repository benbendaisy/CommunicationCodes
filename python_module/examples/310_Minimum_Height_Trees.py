from collections import defaultdict
from typing import List


class Solution:
    """
        A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

        Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

        Return a list of all MHTs' root labels. You can return the answer in any order.

        The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

        Example 1:

        Input: n = 4, edges = [[1,0],[1,2],[1,3]]
        Output: [1]
        Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
        Example 2:

        Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        Output: [3,4]

        Constraints:

        1 <= n <= 2 * 104
        edges.length == n - 1
        0 <= ai, bi < n
        ai != bi
        All the pairs (ai, bi) are distinct.
        The given input is guaranteed to be a tree and there will be no repeated edges.
    """
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]

        # build the graph with the adjacency list
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)

        # handle original leaves
        leaves = []
        for key, value in graph.items():
            if len(value) == 1:
                leaves.append(key)

        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []
            while leaves:
                leave = leaves.pop()
                # the only neighbor left
                neighbor = graph[leave].pop()
                # remove leave from neighbor's neighbors
                graph[neighbor].remove(leave)
                # add neighbors to new leave set
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def helper(node: int, parent: int) -> int:
            depth = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    depth = max(depth, helper(neighbor, node))
            return depth + 1
        heights = [helper(i, -1) for i in range(n)]
        min_height = min(heights)
        return [i for i in range(n) if heights[i] == min_height]
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0] # Only one node, so it's the root
        
        # Step 1: Build adjacency list and degree
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Step 2: Find initial leaf nodes (nodes with only one connection)
        que = deque([node for node in graph if degree[node] == 1])
        # Step 3: Remove leaf nodes layer by layer
        remaining_nodes = n
        while remaining_nodes > 2:
            level_size = len(que)
            remaining_nodes -= level_size
            for _ in range(level_size):
                leaf = que.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        que.append(neighbor)
        return list(que)


