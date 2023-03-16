# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

        Example 1:

        Input: root = [1,2,2,3,4,4,3]
        Output: true
        Example 2:

        Input: root = [1,2,2,null,3,null,3]
        Output: false
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_same(left_node: Optional[TreeNode], right_node: Optional[TreeNode]):
            if not left_node and not right_node:
                return True
            elif not left_node or not right_node or left_node.val != right_node.val:
                return False

            return is_same(left_node.left, right_node.right) and is_same(left_node.right, right_node.left)

        return is_same(root.left, root.right)


