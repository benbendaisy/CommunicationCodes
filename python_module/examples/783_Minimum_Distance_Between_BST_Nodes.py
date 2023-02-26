# Definition for a binary tree node.
import math
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

        Example 1:

        Input: root = [4,2,6,1,3]
        Output: 1
        Example 2:

        Input: root = [1,0,48,null,null,12,49]
        Output: 1
    """
    def minDiffInBST1(self, root: Optional[TreeNode]) -> int:
        data = []
        def in_order_traverse(node):
            if not node:
                return
            in_order_traverse(node.left)
            data.append(node.val)
            in_order_traverse(node.right)

        in_order_traverse(root)
        min_diff = math.inf
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                min_diff = min(min_diff, abs(data[i] - data[j]))
        return min_diff

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev, res = -math.inf, math.inf
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res = min(res, node.val - prev)
            prev = node.val
            node = node.right
        return res
