# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

    Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
    Output: 2
    Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
    Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
    Output: 1
    Explanation: The lowest common ancestor of a single node is the node itself.

    Example 3:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
    Output: 5
    Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
    """
    def lowestCommonAncestor0(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        parents = {root: (None, 0)}  # Store parent and depth
        
        def helper(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if node.left:
                parents[node.left] = (node, depth + 1)
                helper(node.left, depth + 1)
            if node.right:
                parents[node.right] = (node, depth + 1)
                helper(node.right, depth + 1)
        
        helper(root, 0)
        
        parent_path = defaultdict(int)
        
        # Count occurrences of each ancestor
        for node in nodes:
            while node:
                parent_path[node] += 1
                node = parents[node][0]
        
        # Find the deepest node that appears in all paths
        lca, max_depth = root, 0
        for node, count in parent_path.items():
            if count == len(nodes) and parents[node][1] > max_depth:
                max_depth = parents[node][1]
                lca = node
        
        return lca
    
    def lowestCommonAncestor1(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        parents = {root: (None, 0)}
        def helper(node: TreeNode, depth) -> bool:
            if not node:
                return
            if node.left:
                parents[node.left] = (node, depth + 1)
            if node.right:
                parents[node.right] = (node, depth + 1)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        helper(root, 0)
        parent_path = defaultdict(int)
        for node in nodes:
            while node:
                parent_path[node] += 1
                node = parents[node][0]
        lca, dep = root, 0
        for node, cnt in parent_path.items():
            if cnt == len(nodes) and parents[node][1] > dep:
                lca = node
                dep = parents[node][1]
        return lca
    
    def lowestCommonAncestor2(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_set = set(nodes)
        @cache
        def helper(node: TreeNode):
            if not node:
                return None
            
            if node in nodes_set:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            if left and right:
                return node
            return left if left else right
        return helper(root)