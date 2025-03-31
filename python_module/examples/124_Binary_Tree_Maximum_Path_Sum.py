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
        A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

        The path sum of a path is the sum of the node's values in the path.

        Given the root of a binary tree, return the maximum path sum of any non-empty path.

        Example 1:

        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
        Example 2:

        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    """
    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        max_sum_path = -math.inf
        # post order traversal of subtree rooted at `node`
        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_sum_path
            if not node:
                return 0
            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gain_from_left = max(gain_from_subtree(node.left), 0)
            # add the gain / path sum from right subtree. 0 if negative
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            max_sum_path = max(max_sum_path, gain_from_left + gain_from_right + node.val)

            return max(gain_from_left + node.val, gain_from_right + node.val)
        gain_from_subtree(root)
        return max_sum_path
    
    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def max_path_sum(node: TreeNode):
            nonlocal max_sum
            if not node:
                return 0
            left_path = max(max_path_sum(node.left), 0)
            right_path = max(max_path_sum(node.right), 0)
            max_sum = max(max_sum, left_path + right_path + node.val)
            return max(left_path, right_path) + node.val
        max_path_sum(root)
        return max_sum
    
    def maxPathSum3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')
        def helper(node: TreeNode):
            nonlocal max_sum
            if not node:
                return 0
            
            left_path = max(helper(node.left), 0)
            right_path = max(helper(node.right), 0)
            cur_sum = left_path + right_path + node.val
            max_sum = max(max_sum, cur_sum)
            return max(left_path, right_path) + node.val
        helper(root)
        return max_sum
    
    def maxPathSum4(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_sum = float("-inf")
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            cur_sum = left + right + node.val
            self.max_sum = max(self.max_sum, cur_sum)

            return max(left, right) + node.val
        
        helper(root)
        return self.max_sum



