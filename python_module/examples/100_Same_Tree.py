# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Example 1:

        Input: p = [1,2,3], q = [1,2,3]
        Output: true
        Example 2:

        Input: p = [1,2], q = [1,null,2]
        Output: false
        Example 3:

        Input: p = [1,2,1], q = [1,1,2]
        Output: false

    """
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        return self.isSameTree1(p.left, q.left) and self.isSameTree1(p.right, q.right)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        @cache
        def helper(p_node: TreeNode, q_node: TreeNode) -> bool:
            if not p_node and not q_node:
                return True
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            
            return helper(p_node.left, q_node.left) and helper(p_node.right, q_node.right)
        return helper(p, q)