class Solution:
    """
    The diameter of a tree is the number of edges in the longest path in that tree.

    There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

    Return the diameter of the tree.

    Example 1:

    Input: edges = [[0,1],[0,2]]
    Output: 2
    Explanation: The longest path of the tree is the path 1 - 0 - 2.
    Example 2:

    Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    Output: 4
    Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
        """
    def diameter_of_tree(edges):
        # Build the adjacency list representation of the tree
        n = len(edges) + 1  # n nodes require n-1 edges in a tree
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  # Undirected edge
        
        # Global variable to track diameter
        max_diameter = [0]
        
        def dfs(node, parent):
            # Find the two longest paths going through this node
            longest = second_longest = 0
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the parent to avoid cycles
                
                # Get the length of the longest path starting from this neighbor
                path_length = dfs(neighbor, node)
                
                # Update the two longest paths
                if path_length > longest:
                    second_longest = longest
                    longest = path_length
                elif path_length > second_longest:
                    second_longest = path_length
            
            # Update the maximum diameter if the path through this node is longer
            max_diameter[0] = max(max_diameter[0], longest + second_longest)
            
            # Return the length of the longest path starting from this node
            return longest + 1
        
        # Start DFS from any node (we choose node 0)
        dfs(0, -1)
        return max_diameter[0]

    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        max_diameter = [0]
        def helper(node, parent):
            longest = second_longest = 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                path_length = helper(neighbor, node)
                if path_length > longest:
                    second_longest = longest
                    longest = path_length
                elif path_length > second_longest:
                    second_longest = path_length
                
            max_diameter[0] = max(max_diameter[0], longest + second_longest)
            return longest + 1
        
        helper(0, -1)
        return max_diameter[0]