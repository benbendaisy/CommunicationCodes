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
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

        Example 1:

        Input: root = [2,1,3]
        Output: true
        Example 2:

        Input: root = [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -231 <= Node.val <= 231 - 1
    """
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(cur, less_val, bigger_val):
            if not cur:
                return True
            if less_val >= cur.val or cur.val >= bigger_val:
                return False
            return valid_bst(cur.left, less_val, cur.val) and valid_bst(cur.right, cur.val, bigger_val)
        return valid_bst(root, -math.inf, math.inf)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root, float('-inf'), float('inf'))
