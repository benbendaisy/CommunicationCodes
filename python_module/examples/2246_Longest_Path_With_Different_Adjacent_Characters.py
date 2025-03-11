from collections import defaultdict
from typing import List


class Solution:
    """
        You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

        You are also given a string s of length n, where s[i] is the character assigned to node i.

        Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

        Example 1:

        Input: parent = [-1,0,0,1,1,2], s = "abacbe"
        Output: 3
        Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
        It can be proven that there is no longer path that satisfies the conditions.
        Example 2:

        Input: parent = [-1,0,0,0], s = "aabc"
        Output: 3
        Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
    """
    def longestPath1(self, parent: List[int], s: str) -> int:
        # Construct the tree using the parent list.
        tree = defaultdict(list)
        for end, start in enumerate(parent):
            tree[start].append(end)
        # Store the longest path
        # It is updated in dfs
        res = 1

        # dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
        def dfs(node):
            nonlocal res
            # While examing the children,
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node
            # in the sub-tree rooted at this node.
            max1 = max2 = 0

            for neighbor in tree[node]:
                max_path = dfs(neighbor)
                # This condition makes sure the path is valid.
                if s[node] != s[neighbor]:
                    # Update the length of the top two longest paths.
                    if max_path > max1:
                        max2 = max1
                        max1 = max_path
                    elif max_path > max2:
                        max2 = max_path
            # Update the result.
            # Again, max1+max2+1 means the length of the longest valid path
            # going through this node in the sub-tree rooted at this node.
            res = max(res, max1 + max2 + 1)

            # Adding 1 for the current node
            return max1 + 1
        dfs(0)
        return res
    
    def longestPath2(self, parent: List[int], s: str) -> int:
        # Step 1: Construct the graph as an adjacency list
        graph = defaultdict(list)
        for child, par in enumerate(parent):
            if par != -1:
                graph[par].append(child)
        
        self.max_length = 0  # To store the longest valid path
        
        # Step 2: DFS function to return the longest path from a node downwards
        def dfs(node: int) -> int:
            longest1, longest2 = 0, 0  # Store top two longest valid paths

            for neighbor in graph[node]:
                path_length = dfs(neighbor)  # Recursive DFS call

                if s[neighbor] != s[node]:  # Only consider if characters differ
                    if path_length > longest1:
                        longest2 = longest1
                        longest1 = path_length
                    elif path_length > longest2:
                        longest2 = path_length

            # Update global max path (including both longest children)
            self.max_length = max(self.max_length, longest1 + longest2 + 1)

            return longest1 + 1  # Return longest path including current node

        dfs(0)  # Start DFS from root (node 0)
        return self.max_length
    
    def longestPath3(self, parent: List[int], s: str) -> int:
        # Step 1: Construct the graph as an adjacency list
        graph = defaultdict(list)
        for child, par in enumerate(parent):
            graph[par].append(child)
        
        self.max_length = 0  # To store the longest valid path
        
        # Step 2: DFS function to return the longest path from a node downwards
        def helper(node: int) -> int:
            longest1, longest2 = 0, 0  # Store top two longest valid paths

            for neighbor in graph[node]:
                path_length = helper(neighbor)  # Recursive DFS call

                if s[neighbor] != s[node]:  # Only consider if characters differ
                    if path_length > longest1:
                        longest2 = longest1
                        longest1 = path_length
                    elif path_length > longest2:
                        longest2 = path_length

            # Update global max path (including both longest children)
            self.max_length = max(self.max_length, longest1 + longest2 + 1)

            return longest1 + 1  # Return longest path including current node

        helper(0)  # Start DFS from root (node 0)
        return self.max_length
    
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for child, par in enumerate(parent):
            graph[par].append(child)
        self.max_len = 0
        @cache
        def helper(node: int) -> int:
            longest1, longest2 = 0, 0
            for neighbor in graph[node]:
                path_len = helper(neighbor)
                if s[neighbor] != s[node]:
                    if path_len > longest1:
                        longest2 = longest1
                        longest1 = path_len
                    elif path_len > longest2:
                        longest2 = path_len
            self.max_len = max(self.max_len, longest1 + longest2 + 1)
            return longest1 + 1
        helper(0)
        return self.max_len