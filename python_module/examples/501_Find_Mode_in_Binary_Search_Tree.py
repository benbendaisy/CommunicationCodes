# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def helper(node):
            if not node:
                return
            counter[node.val] += 1
            helper(node.left)
            helper(node.right)
        helper(root)
        max_freq = max(counter.values())
        res = []
        for key in counter:
            if counter[key] == max_freq:
                res.append(key)
        return res