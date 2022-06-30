# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

        Return the minimum number of cameras needed to monitor all nodes of the tree.

        Example 1:

        Input: root = [0,0,null,0,0]
        Output: 1
        Explanation: One camera is enough to monitor all nodes if placed as shown.
        Example 2:

        Input: root = [0,0,null,0,null,0,null,null,0]
        Output: 2
        Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

        Constraints:

        The number of nodes in the tree is in the range [1, 1000].
        Node.val == 0
    """
    def minCameraCover1(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        covered = {None}

        def dfs(node: TreeNode, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if not parent and node not in covered or node.left not in covered or node.right not in covered:
                    self.cnt += 1
                    covered.update({node, parent, node.left, node.right})
        dfs(root)
        return self.cnt