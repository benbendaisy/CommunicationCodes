from collections import defaultdict, Counter
from typing import List


class Solution:
    """
    You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

    The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

    Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

    A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

    Example 1:

    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
    Output: [2,1,1,1,1,1,1]
    Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
    Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
    Example 2:

    Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
    Output: [4,2,1,1]
    Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
    The sub-tree of node 3 contains only node 3, so the answer is 1.
    The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
    The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
    Example 3:

    Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
    Output: [3,2,1,1,1]
    """
    def countSubTrees1(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([0])
        def dfs(node):
            c = Counter(labels[node])
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                c += dfs(neighbor)
            ans[node] = c.get(labels[node])
            return c
        dfs(0)
        return ans
    
    def countSubTrees2(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = [0] * n
        
        def helper(node: int, parent: int) -> dict:
            # Create a frequency counter for each character
            char_dict = defaultdict(int)
            
            # Add current node's label
            current_label = labels[node]
            char_dict[current_label] += 1
            
            # Process all neighbors except parent
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Get character counts from child subtree
                    child_dict = helper(neighbor, node)
                    
                    # Merge child counts with current node's counts
                    for char, count in child_dict.items():
                        char_dict[char] += count
            
            # Store result for this node (number of nodes with same label in subtree)
            res[node] = char_dict[current_label]
            
            return char_dict
        
        helper(0, -1)
        return res

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = [0] * n
        def helper(node: int, parent: int):
            char_dict = defaultdict(int)
            current_label = labels[node]
            char_dict[current_label] = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    child_dict = helper(neighbor, node)
                    for ch, cnt in child_dict.items():
                        char_dict[ch] += cnt
            res[node] = char_dict[current_label]
            return char_dict
        
        helper(0, -1)
        return res

