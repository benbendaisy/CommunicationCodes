# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

    Example 1:

    Input: root = [1,3,2,5,3,null,9]
    Output: [1,3,9]
    Example 2:

    Input: root = [1,2,3]
    Output: [1,3]
    """
    def largestValues1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        que = deque([root])
        while que:
            cur_length = len(que)
            cur_max = float("-inf")
            for _ in range(cur_length):
                node = que.popleft()
                cur_max = max(cur_max, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(cur_max)
        return res
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        @cache
        def helper(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        helper(root, 0)
        return res