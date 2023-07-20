# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

    Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

    Example 1:

    Input: root = [1,7,0,7,-8,null,null]
    Output: 2
    Explanation: 
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.
    Example 2:

    Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    Output: 2
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_dict = defaultdict(list)
        def level_traveller(node, level):
            if not node:
                return
            level_dict[level].append(node.val)
            level_traveller(node.left, level + 1)
            level_traveller(node.right, level + 1)
        level_traveller(root, 1)
        max_sum, max_level = -float("inf"), 1
        for key in level_dict.keys():
            t = sum(level_dict[key])
            if t > max_sum:
                max_sum = t
                max_level = key
        return max_level
