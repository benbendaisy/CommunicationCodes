# Definition for a binary tree node.
from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

    Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

    A full binary tree is a binary tree where each node has exactly 0 or 2 children

    Example 1:

    Input: n = 7
    Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    Example 2:

    Input: n = 3
    Output: [[0,0,0]]
    """
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def helper(k):
            if k == 0:
                return []
            elif k == 1:
                return [TreeNode(0)]
            return [TreeNode(0, left, right) for i in range(1, k, 2) for left in helper(i) for right in helper(k - i - 1)]
        return helper(n)
    
    def allPossibleFBT1(self, n: int) -> List[Optional[TreeNode]]:
        memory = {0: [], 1: [TreeNode(0)]}
        def helper(k):
            if k not in memory:
                memory[k] = [TreeNode(0, left, right) for i in range(1, k, 2) for left in helper(i) for right in helper(k - i - 1)]
            return memory[k]
        return helper(n)