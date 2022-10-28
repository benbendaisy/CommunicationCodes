# Definition for a binary tree node.
from functools import lru_cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def processSubTrees(node, isLeft):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val if isLeft else 0

            return processSubTrees(node.left, True) + processSubTrees(node.right, False)

        return processSubTrees(root, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if isLeaf(node.left):
                res += node.left.val

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)
        return res
