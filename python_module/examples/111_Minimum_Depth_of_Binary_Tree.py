
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @lru_cache(None)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return 1 + min(left, right)
        return 1 + max(left, right)
    
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level, stack = 0, deque([root])
        while stack:
            level += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return level
            