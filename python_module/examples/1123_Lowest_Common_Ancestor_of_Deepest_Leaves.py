# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        

        def helper(node: TreeNode):
            if not node:
                return 0, None
            dep_left, dep_left_lca = helper(node.left)
            dep_right, dep_right_lca = helper(node.right)

            if dep_left > dep_right:
                return dep_left + 1, dep_left_lca
            elif dep_right > dep_left:
                return dep_right + 1, dep_right_lca
            
            return dep_left + 1, node
        
        return helper(root)[1]
    
    def lcaDeepestLeaves2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None  # depth, LCA
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            else:
                return left_depth + 1, node  # This node is the LCA

        return dfs(root)[1]  # Extract the LCA from the tuple
    
    def lcaDeepestLeaves3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def helper(node: TreeNode):
            if not node:
                return (0, None)
            
            left_dep, left_lca = helper(node.left)
            right_dep, right_lca = helper(node.right)

            if left_dep > right_dep:
                return (left_dep + 1, left_lca)
            elif right_dep > left_dep:
                return (right_dep + 1, right_lca)
            
            return (left_dep + 1, node)
        
        return helper(root)[1]
    
    def lcaDeepestLeaves4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        @cache
        def helper(node: TreeNode):
            if not node:
                return (0, None)
            
            dep_left, lca_left = helper(node.left)
            dep_right, lca_right = helper(node.right)

            if dep_left > dep_right:
                return dep_left + 1, lca_left
            elif dep_left < dep_right:
                return dep_right + 1, lca_right
            return dep_left + 1, node
        return helper(root)[1]
