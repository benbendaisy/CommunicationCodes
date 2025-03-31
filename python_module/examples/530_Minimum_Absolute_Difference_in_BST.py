# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

    Example 1:

    Input: root = [4,2,6,1,3]
    Output: 1
    Example 2:

    Input: root = [1,0,48,null,null,12,49]
    Output: 1
    """
    def __init__(self):
        self.min_diff = float('inf')
        self.prev_val = None
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        def in_order_traverse(node):
            if not node:
                return
            in_order_traverse(node.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
            self.prev_val = node.val
            in_order_traverse(node.right)
        in_order_traverse(root)
        return self.min_diff

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        prev_val = None
        min_diff = float('inf')
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev_val is not None:
                min_diff = min(min_diff, abs(cur.val - prev_val))
            prev_val = cur.val
            cur = cur.right
        return min_diff
    
    def getMinimumDifference3(self, root: Optional[TreeNode]) -> int:
        self.prev = None  # To keep track of the last visited node in in-order traversal
        self.min_diff = float('inf')

        def in_order_traversal(node: Optional[TreeNode]):
            if not node:
                return
            
            # Traverse left subtree
            in_order_traversal(node.left)
            
            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update previous node
            
            # Traverse right subtree
            in_order_traversal(node.right)

        in_order_traversal(root)
        return self.min_diff
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float("inf")
        def helper(node: TreeNode):
            if not node:
                return
            helper(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(self.prev - node.val))
            self.prev = node.val
            helper(node.right)
        
        helper(root)
        return self.min_diff