# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

        A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

        Example 1:

        Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
        Output: 7
        Explanation: We have various ancestor-node differences, some of which are given below :
        |8 - 3| = 5
        |3 - 7| = 4
        |8 - 1| = 7
        |10 - 13| = 3
        Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
        Example 2:

        Input: root = [1,null,2,null,0,3]
        Output: 3
    """
    def maxAncestorDiff1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        def helper(node, cur_min, cur_max):
            if not node:
                return
            self.res = max(self.res, abs(node.val - cur_min), abs(node.val - cur_max))
            cur_min = min(cur_min, node.val)
            cur_max = min(cur_max, node.val)
            helper(node.left, cur_min, cur_max)
            helper(node.right, cur_min, cur_max)
        helper(root, root.val, root.val)
        return self.res
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def helper(node, min_v, max_v):
            nonlocal res
            if not node:
                return
            res = max(res, abs(node.val - min_v), abs(node.val - max_v))
            min_v = min(node.val, min_v)
            max_v = max(node.val, max_v)
            helper(node.left, min_v, max_v)
            helper(node.right, min_v, max_v)
        helper(root, root.val, root.val)
        return res