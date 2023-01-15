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
    def longestPath(self, parent: List[int], s: str) -> int:
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