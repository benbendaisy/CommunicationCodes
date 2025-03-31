# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

        Example 1:

        Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        Output: [3,9,20,null,null,15,7]
        Example 2:

        Input: inorder = [-1], postorder = [-1]
        Output: [-1]
    """
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node_cache = {v : i for i, v in enumerate(inorder)}
        def build_tree(in_start, in_end, post_end):
            if in_start > in_end or post_end < 0:
                return None
            root = TreeNode(postorder[post_end])
            in_idx = node_cache[root.val]
            root.right = build_tree(in_idx + 1, in_end, post_end - 1)
            root.left = build_tree(in_start, in_idx - 1, post_end - (in_end - in_idx) - 1)
            return root

        return build_tree(0, len(inorder) - 1, len(postorder) - 1)
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos_dict = {v:i for i,v in enumerate(inorder)}
        
        def helper(in_s: int, in_e: int, po_e: int) -> Optional[TreeNode]:
            if in_s > in_e or po_e < 0:
                return None
            node = TreeNode(postorder[po_e])
            pos = pos_dict[postorder[po_e]]
            left_length = in_e - pos
            node.left = helper(in_s, pos - 1, po_e - left_length - 1)
            node.right = helper(pos + 1, in_e, po_e - 1)
            return node
        return helper(0, len(inorder) - 1, len(postorder) - 1)

