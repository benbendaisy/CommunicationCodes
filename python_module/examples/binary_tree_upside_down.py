# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        node, parent, parentRight = root, None, None
        while node:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left

        return parent

    def upsideDownBinaryTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        new_root = self.upsideDownBinaryTree(root.left)
        left = root.left
        right = root.right
        left.left = right
        left.right = root
        root.left = root.right = None
        return new_root