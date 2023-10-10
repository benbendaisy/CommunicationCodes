# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

        Example 1:

        Input: root = [1,2,3,null,5,null,4]
        Output: [1,3,4]
        Example 2:

        Input: root = [1,null,3]
        Output: [1,3]
        Example 3:

        Input: root = []
        Output: []

        Constraints:

        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level_map = defaultdict(list)
        que = deque([(root, 0)])
        while que:
            node, level = que.popleft()
            if node:
                level_map[level].append(node)
                que.append((node.left, level + 1))
                que.append((node.right, level + 1))
        res = []
        for key in sorted(level_map.keys()):
            cur = level_map[key][-1]
            res.append(cur.val)
        return res