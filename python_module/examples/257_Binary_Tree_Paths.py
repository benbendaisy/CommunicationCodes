# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        def tree_paths(node: TreeNode, path: list):
            if node and not node.left and not node.right:
                res.append("->".join([str(x) for x in path + [node.val]]))
                return
            if node.left:
                tree_paths(node.left, path + [node.val])
            if node.right:
                tree_paths(node.right, path + [node.val])
        tree_paths(root, [])
        return res