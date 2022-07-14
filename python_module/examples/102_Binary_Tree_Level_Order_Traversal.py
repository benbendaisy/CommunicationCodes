# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

        Example 1:

        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        Example 2:

        Input: root = [1]
        Output: [[1]]
        Example 3:

        Input: root = []
        Output: []
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        levelMap = defaultdict(list)
        while queue:
            node, row = queue.popleft()
            if node:
                queue.append((node.left, row + 1))
                queue.append((node.right, row + 1))
                levelMap[row].append(node.val)

        return [levelMap[key] for key in sorted(levelMap.keys())]