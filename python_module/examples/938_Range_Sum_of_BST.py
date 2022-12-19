# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

        Example 1:

        Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
        Output: 32
        Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
        Example 2:

        Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
        Output: 23
        Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
    """
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def range_sum_bst(node: TreeNode):
            if not node:
                return 0

            new_sum = 0
            if low <= node.val <= high:
                new_sum += node.val
            if node.left:
                new_sum += range_sum_bst(node.left)
            if node.right:
                new_sum += range_sum_bst(node.right)
            return new_sum
        return range_sum_bst(root)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans

