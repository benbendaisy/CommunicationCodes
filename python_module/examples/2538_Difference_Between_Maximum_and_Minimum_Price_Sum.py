class Solution:
    """
    There exists an undirected and initially unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

    The price sum of a given path is the sum of the prices of all nodes lying on that path.

    The tree can be rooted at any node root of your choice. The incurred cost after choosing root is the difference between the maximum and minimum price sum amongst all paths starting at root.

    Return the maximum possible cost amongst all possible root choices.

    Example 1:

    Input: n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
    Output: 24
    Explanation: The diagram above denotes the tree after rooting it at node 2. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum.
    - The first path contains nodes [2,1,3,4]: the prices are [7,8,6,10], and the sum of the prices is 31.
    - The second path contains the node [2] with the price [7].
    The difference between the maximum and minimum price sum is 24. It can be proved that 24 is the maximum cost.
    Example 2:

    Input: n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
    Output: 2
    Explanation: The diagram above denotes the tree after rooting it at node 0. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum.
    - The first path contains nodes [0,1,2]: the prices are [1,1,1], and the sum of the prices is 3.
    - The second path contains node [0] with a price [1].
    The difference between the maximum and minimum price sum is 2. It can be proved that 2 is the maximum cost.
    """
    def maxOutput1(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # Step 1: Construct adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.max_cost = 0  # Store the maximum cost across all possible roots

        # Step 2: DFS function to compute max and min path sums for a given root
        @lru_cache(None)
        def dfs(node: int, parent: int) -> tuple:
            """ Returns (max_path_sum, min_path_sum) for a subtree rooted at `node`. """
            max_path, min_path = price[node], price[node]  # Start with node's price
            
            for neighbor in graph[node]:
                if neighbor == parent:  # Avoid revisiting parent
                    continue
                child_max, child_min = dfs(neighbor, node)
                
                # Extend the paths with the current node
                max_path = max(max_path, price[node] + child_max)
                min_path = min(min_path, price[node] + child_min)

            return (max_path, min_path)

        # Step 3: Try each node as root and compute the cost
        for root in range(n):
            max_sum, min_sum = dfs(root, -1)
            self.max_cost = max(self.max_cost, max_sum - min_sum)

        return self.max_cost
    
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        if not edges:
            return 0
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def helper(node: int, parent: int) -> tuple:
            if node == -1:
                return (0, 0)
            
            path_min, path_max = price[node], price[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    path_node_min, path_node_max = helper(neighbor, node)
                    path_min = min(path_min, path_node_min + price[node])
                    path_max = max(path_max, path_node_max + price[node])
            return (path_min, path_max)
        max_cost = float('-inf')
        for i in range(n):
            path_min, path_max = helper(i, -1)
            max_cost = max(max_cost, path_max - path_min)
        return 0 if max_cost == float('-inf') else max_cost