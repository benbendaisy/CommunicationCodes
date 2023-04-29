# Definition for a binary tree node.
import math
from collections import deque, defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, return the maximum width of the given tree.

        The maximum width of a tree is the maximum width among all levels.

        The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

        It is guaranteed that the answer will in the range of a 32-bit signed integer.

        Example 1:

        Input: root = [1,3,2,5,3,null,9]
        Output: 4
        Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
        Example 2:

        Input: root = [1,3,2,5,null,null,9,6,null,7]
        Output: 7
        Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
        Example 3:

        Input: root = [1,3,2,5]
        Output: 2
        Explanation: The maximum width exists in the second level with length 2 (3,2).
    """
    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0, 0)])
        max_left, max_right = -math.inf, math.inf
        level_dict = defaultdict(lambda : (0, 0))
        while queue:
            node, level, width = queue.popleft()
            if not node:
                continue
            max_left = max(level_dict[level][0], width)
            max_right = min(level_dict[level][1], width)
            level_dict[level] = (max_left, max_right)
            queue.append((node.left, level + 1, width + 1))
            queue.append((node.right, level + 1, width - 1))
        max_width = 1
        for left, right in level_dict.values():
            max_width = max(max_width, right - left + 1)
        return max_width

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_width = 0
        while queue:
            level_length = len(queue)
            _, start_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            max_width = max(max_width, index - start_index + 1)
        return max_width