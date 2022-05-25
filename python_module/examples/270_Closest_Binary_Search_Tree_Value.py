# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    """
        Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

        Example 1:

        Input: root = [4,2,5,1,3], target = 3.714286
        Output: 4
        Example 2:

        Input: root = [1], target = 4.428571
        Output: 1

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        0 <= Node.val <= 109
        -109 <= target <= 109

    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.val = math.inf

    def closestValue1(self, root: Optional[TreeNode], target: float) -> int:
        def inorderTraverse(cur: Optional[TreeNode]):
            if not cur:
                return

            inorderTraverse(cur.left)
            self.val = cur.val if abs(cur.val - target) < abs(self.val - target) else self.val
            inorderTraverse(cur.right)

        inorderTraverse(root)
        return self.val

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inOrderTraverse(cur: Optional[TreeNode]):
            return inOrderTraverse(cur.left) + [cur.val] + inOrderTraverse(cur.right) if cur else []

        return min(inOrderTraverse(root), key = lambda x: abs(target - x))
