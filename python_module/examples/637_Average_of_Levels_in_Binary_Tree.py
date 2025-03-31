# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

        Example 1:

        Input: root = [3,9,20,null,null,15,7]
        Output: [3.00000,14.50000,11.00000]
        Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
        Hence return [3, 14.5, 11].
        Example 2:

        Input: root = [3,9,20,15,7]
        Output: [3.00000,14.50000,11.00000]

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -231 <= Node.val <= 231 - 1
    """
    def averageOfLevels1(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = deque([(root, 0)])
        levelDict = defaultdict(list)
        while queue:
            node, level = queue.popleft()
            levelDict[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        res = []
        for val in levelDict.values():
            res.append(sum(val) / len(val))

        return res

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        pos_dict = defaultdict(list)
        def helper(node: TreeNode, dep: int):
            if not node:
                return
            pos_dict[dep].append(node.val)
            helper(node.left, dep + 1)
            helper(node.right, dep + 1)
        helper(root, 0)
        res = []
        for level in pos_dict.values():
            res.append(sum(level) * 1.0 / len(level))
        
        return res
