class Solution:
    """
    A tree rooted at node 0 is given as follows:

    The number of nodes is nodes;
    The value of the ith node is value[i];
    The parent of the ith node is parent[i].
    Remove every subtree whose sum of values of nodes is zero.

    Return the number of the remaining nodes in the tree.

    Example 1:

    Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
    Output: 2
    Example 2:

    Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
    Output: 6
    """
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        if not parent:
            return 0
        
        n = len(parent)
        # Build adjacency list (tree structure)
        graph = defaultdict(list)
        for cld, prt in enumerate(parent):
            if prt != -1: # Ignore root (-1 has no parent)
                graph[prt].append(cld)
        
        @cache
        def helper(node: int):
            """Returns (subtree sum, count of remaining nodes)"""
            total_sum, total_cnt = value[node], 1 # Count this node initially
            for neighbor in graph[node]: # Traverse all children
                child_sum, child_cnt = helper(neighbor)
                total_sum += child_sum
                total_cnt += child_cnt
            return (total_sum, total_cnt if total_sum != 0 else 0) # Delete subtree if sum == 0
        
        # Root node is always at index 0
        return helper(0)[-1]