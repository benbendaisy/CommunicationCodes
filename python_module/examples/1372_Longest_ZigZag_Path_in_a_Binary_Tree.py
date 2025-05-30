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
    You are given the root of a binary tree.

    A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.
    Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

    Return the longest ZigZag path contained in that tree.

    Example 1:

    Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
    Output: 3
    Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
    Example 2:

    Input: root = [1,1,1,null,1,null,null,1,1,null,1]
    Output: 4
    Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
    Example 3:

    Input: root = [1]
    Output: 0
    """
    def longestZigZag1(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node):
            #  For each node, it computes three values: the length of
            #  the longest zigzag path starting from the node and going
            #  left, the length of the longest zigzag path starting from
            #  the node and going right, and the maximum length of zigzag
            #  path found so far in the tree.
            if not node:
                return [-1, -1, -1]
            left, right = dfs(node.left), dfs(node.right)
            return [
                left[1] + 1, # go right to pick 1
                right[0] + 1, # go left to pick 0
                # pick the max of left, right, previous left and previous right
                max(left[1] + 1, right[0] + 1, left[2], right[2])
            ]
        return dfs(root)[-1]
    
    def longestZigZag2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_dep = 0
        @cache
        def helper(node: TreeNode, is_left: bool, depth: int):
            if not node:
                return
            
            self.max_dep = max(self.max_dep, depth)
            if is_left:
                helper(node.right, False, depth + 1)
                helper(node.left, True, 1)
            else:
                helper(node.left, True, depth + 1)
                helper(node.right, False, 1)
            
        helper(root.left, True, 1)
        helper(root.right, False, 1)
        return self.max_dep
    
    def longestZigZag3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node: TreeNode):
            if not node:
                return (-1, -1, -1)
            
            left = helper(node.left)
            right = helper(node.right)

            return (
                left[1] + 1,
                right[0] + 1,
                max(left[1] + 1, right[0] + 1, left[2], right[2])
            )
        
        return helper(root)[-1]
    
    def longestZigZag4(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node: TreeNode):
            if not node:
                return (-1, -1, -1)
            
            left = helper(node.left)
            right = helper(node.right)

            return (
                left[1] + 1,
                right[0] + 1,
                max(left[1] + 1, right[0] + 1, left[2], right[2])
            )
        
        return helper(root)[-1]

