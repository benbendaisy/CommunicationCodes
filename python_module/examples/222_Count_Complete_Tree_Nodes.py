# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a complete binary tree, return the number of the nodes in the tree.

        According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

        Design an algorithm that runs in less than O(n) time complexity.

        Example 1:

        Input: root = [1,2,3,4,5,6]
        Output: 6
        Example 2:

        Input: root = []
        Output: 0
        Example 3:

        Input: root = [1]
        Output: 1
    """
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        cnt = 0
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right
            cnt += 1
        return cnt

