class Solution:
    """
    Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:

    Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
    He tells Alice that u is the parent of v in the tree.
    Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.

    Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.

    Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.

    Example 1:

    Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
    Output: 3
    Explanation: 
    Root = 0, correct guesses = [1,3], [0,1], [2,4]
    Root = 1, correct guesses = [1,3], [1,0], [2,4]
    Root = 2, correct guesses = [1,3], [1,0], [2,4]
    Root = 3, correct guesses = [1,0], [2,4]
    Root = 4, correct guesses = [1,3], [1,0]
    Considering 0, 1, or 2 as root node leads to 3 correct guesses.

    Example 2:

    Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
    Output: 5
    Explanation: 
    Root = 0, correct guesses = [3,4]
    Root = 1, correct guesses = [1,0], [3,4]
    Root = 2, correct guesses = [1,0], [2,1], [3,4]
    Root = 3, correct guesses = [1,0], [2,1], [3,2], [3,4]
    Root = 4, correct guesses = [1,0], [2,1], [3,2]
    Considering any node as root will give at least 1 correct guess. 
    """
    def rootCount1(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # Step 1: Build the tree using an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Convert guesses to a set of tuples for quick lookup
        guesses_set = set((u, v) for u, v in guesses)
        
        # Step 2: Initialize the result
        result = 0
        
        # Step 3: Recursive function to count correct guesses
        @cache
        def dfs(node, parent, correct_guesses):
            count = 0
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                if (node, neighbor) in guesses_set:
                    count += 1
                count += dfs(neighbor, node, correct_guesses)
            return count
        
        # Step 4: Iterate over all nodes and count correct guesses
        for node in tree:
            correct_guesses = dfs(node, -1, 0)
            if correct_guesses >= k:
                result += 1
        
        return result
    
    def rootCount2(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        guess_set = {(u, v) for u, v in guesses}

        @cache
        def helper(node: int, parent: int):
            cnt = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if (node, neighbor) in guess_set:
                    cnt += 1
                cnt += helper(neighbor, node)
            return cnt
        
        res = 0
        for node in graph:
            correct_guesses = helper(node, -1)
            if correct_guesses >= k:
                res += 1
        return res
    
