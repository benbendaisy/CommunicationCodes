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
        def treePaths(cur, path):
            if cur and not cur.left and not cur.right:
                res.append("->".join([str(x) for x in path + [cur.val]]))
                return
            if cur.left:
                treePaths(cur.left, path + [cur.val])
            if cur.right:
                treePaths(cur.right, path + [cur.val])

        treePaths(root, [])
        return res