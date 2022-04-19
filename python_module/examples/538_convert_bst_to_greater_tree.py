# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = []
        cur = root
        total = 0
        while len(stack) > 0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            total += cur.val
            cur.val = total
            cur = cur.left
        return root

