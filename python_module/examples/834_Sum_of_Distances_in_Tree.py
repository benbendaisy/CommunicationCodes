class Solution:
    """
    There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

    Example 1:

    Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
    Explanation: The tree is shown above.
    We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
    equals 1 + 1 + 2 + 2 + 2 = 8.
    Hence, answer[0] = 8, and so on.
    Example 2:

    Input: n = 1, edges = []
    Output: [0]
    Example 3:

    Input: n = 2, edges = [[1,0]]
    Output: [1,1]
    """ 
    def sumOfDistancesInTree1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize arrays
        count = [1] * n  # count[i] = number of nodes in subtree rooted at i
        result = [0] * n  # result[i] = sum of distances from node i to all other nodes
        
        # First DFS: post-order traversal to compute count and partial results
        def dfs1(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    count[node] += count[neighbor]
                    result[node] += result[neighbor] + count[neighbor]
        
        # Second DFS: pre-order traversal to compute final results
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    # When we move from parent to child, we remove child subtree nodes and add remaining nodes
                    result[neighbor] = result[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor, node)
        
        # Run the two DFS
        dfs1(0, -1)  # Start from node 0 as root
        dfs2(0, -1)
        
        return result
    
    def sumOfDistancesInTree2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, no distance

        # Step 1: Build the adjacency list representation of the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Initialize storage arrays
        answer = [0] * n     # Stores sum of distances for each node
        subtree_size = [0] * n  # Stores subtree size for each node

        # Step 3: First DFS - Compute subtree sizes and initial distances
        def postorder(node: int, parent: int):
            subtree_size[node] = 1  # Count itself
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                postorder(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]
                answer[node] += answer[neighbor] + subtree_size[neighbor]
        
        postorder(0, -1)  # Start from node 0

        # Step 4: Second DFS - Compute distances for all nodes
        def preorder(node: int, parent: int):
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                # Recalculate answer for child using the parent's result
                answer[neighbor] = answer[node] + (n - 2 * subtree_size[neighbor])
                preorder(neighbor, node)
        
        preorder(0, -1)  # Start from node 0

        return answer
    
    def sumOfDistancesInTree3(n, edges):
        """
        Calculate the sum of distances from each node to all other nodes in an undirected tree.
        
        Args:
            n: Number of nodes in the tree (labeled from 0 to n-1)
            edges: List of edges, where edges[i] = [ai, bi] indicates an edge between nodes ai and bi
            
        Returns:
            An array where answer[i] is the sum of distances from node i to all other nodes
        """
        # Build the adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize arrays to store:
        # - count[i]: number of nodes in the subtree rooted at i (including i)
        # - answer[i]: sum of distances from node i to all other nodes
        count = [1] * n
        answer = [0] * n
        
        def dfs1(node, parent):
            """
            First pass: compute count and partial answer for the root.
            For each node, calculate:
            1. The size of its subtree (count)
            2. The sum of distances to all nodes in its subtree
            """
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]
        
        def dfs2(node, parent):
            """
            Second pass: compute the final answer for all nodes.
            For each node, re-root the tree at that node and update the answer.
            """
            for child in graph[node]:
                if child != parent:
                    # When we re-root the tree from parent to child:
                    # 1. We remove child's subtree from parent (reducing distance by count[child])
                    # 2. We add parent's subtree to child (increasing distance by n - count[child])
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        
        # Start DFS from node 0 (arbitrarily chosen as root)
        dfs1(0, -1)
        dfs2(0, -1)
        
        return answer
    
    def sumOfDistancesInTree4(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        ans = [0 for _ in range(n)]

        sizes = [1 for _ in range(n)]
        def dfs(u, fa, depth):
            ans[0] += depth
            for v in graph[u]:
                if v == fa:
                    continue
                dfs(v, u, depth + 1)
                sizes[u] += sizes[v]

        def reroot(u, fa):
            for v in graph[u]:
                if v == fa:
                    continue
                ans[v] = ans[u] + n - 2 * sizes[v]
                reroot(v, u)

        dfs(0, -1, 0)
        reroot(0, -1)
        return ans
    
    def sumOfDistancesInTree5(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, no distance

        # Step 1: Build the adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Initialize storage arrays
        res = [0] * n
        subtree_cnt = [1] * n

        # Step 3: First DFS - Compute subtree sizes and initial distances
        def post_order(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                post_order(child, node)
                subtree_cnt[node] += subtree_cnt[child]
                res[node] += res[child] + subtree_cnt[child]
        
        post_order(0, -1)  # Start from node 0

        # Step 4: Second DFS - Compute distances for all nodes
        def pre_order(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                res[child] = res[node] - subtree_cnt[child] + n - subtree_cnt[child]
                pre_order(child, node)
        pre_order(0, -1)
        return res
    
    def sumOfDistancesInTree6(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = [0] * n
        subtree_cnt = [1] * n
        def pre_order(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                pre_order(child, node)
                subtree_cnt[node] += subtree_cnt[child]
                res[node] += res[child] + subtree_cnt[child]
        
        pre_order(0, -1)
        def post_order(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue
                res[child] = (res[node] - subtree_cnt[child]) + (n - subtree_cnt[child])
                post_order(child, node)
        
        post_order(0, -1)
        return res