# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees1(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(start, end):
            if start > end:
                return [None]
            ans = []
            for i in range(start, end + 1):
                left = dfs(start, i - 1)
                right = dfs(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        return dfs(1, n)
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def helper(start: int, end: int):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                for l_node in helper(start, i - 1):
                    for r_node in helper(i + 1, end):
                        node = TreeNode(i)
                        node.left = l_node
                        node.right = r_node
                        res.append(node)
            return res
        
        return helper(1, n)