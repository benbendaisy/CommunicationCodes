# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    Example 2:

    Input: root = [2,1,3]
    Output: [2,3,1]
    Example 3:

    Input: root = []
    Output: []
    """
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree1(root.left)
        self.invertTree1(root.right)
        t = root.left
        root.left = root.right
        root.right = t
        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        @cache
        def helper(node: TreeNode):
            if not node:
                return None
            left = helper(node.right)
            right = helper(node.left)
            
            node.left = left
            node.right = right
            return node
        return helper(root)

