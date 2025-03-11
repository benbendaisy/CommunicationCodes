# Definition for a binary tree node.
from functools import lru_cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

        Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

        Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

        Example 1:

        Input: root = [3,2,3,null,3,null,1]
        Output: 7
        Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
        Example 2:

        Input: root = [3,4,5,1,3,null,1]
        Output: 9
        Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        0 <= Node.val <= 104
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def robHelper(node):
            if not node:
                return (0, 0)

            left = robHelper(node.left)
            right = robHelper(node.right)

            # rob the current node
            robbed = node.val + left[1] + right[1]
            notRob = max(left) + max(right)

            return (robbed, notRob)

        return max(robHelper(root))
    
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        @cache
        def helper(node: TreeNode):
            """
            the return type is tuple with the format (not rob, rob) the root node
            """
            if not node:
                return (0, 0)
            left_path = helper(node.left)
            right_path = helper(node.right)
            # If we do NOT rob this node, we can take the best of each child's robbed or not robbed state
            not_robbed = max(left_path) + max(right_path)
            # If we rob this node, we can't rob children, so take only their 'not_robbed' values
            robbed = left_path[0] + right_path[0] + node.val
            return (not_robbed, robbed)
        return max(helper(root))