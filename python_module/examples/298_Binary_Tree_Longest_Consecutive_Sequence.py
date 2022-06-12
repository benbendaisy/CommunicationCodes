# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a binary tree, return the length of the longest consecutive sequence path.

        The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

        Example 1:

        Input: root = [1,null,3,2,4,null,null,null,5]
        Output: 3
        Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
        Example 2:

        Input: root = [2,null,3,2,null,1]
        Output: 2
        Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


        Constraints:

        The number of nodes in the tree is in the range [1, 3 * 104].
        -3 * 104 <= Node.val <= 3 * 104
    """
    def longestConsecutive1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        longestCons = 0
        while q:
            node, d = q.popleft()
            longestCons = max(longestCons, d)
            if node.left:
                if node.left.val == node.val + 1:
                    q.append((node.left, d + 1))
                else:
                    q.append((node.left, 1))

            if node.right:
                if node.right.val == node.val + 1:
                    q.append((node.right, d + 1))
                else:
                    q.append((node.right, 1))

        return longestCons

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.longestDistance = 0
        def longestCons(cur: TreeNode, parent: TreeNode, distance: int):
            if not cur:
                self.longestDistance = max(self.longestDistance, distance)
                return
            length = distance + 1 if parent.val + 1 == cur.val else 1
            self.longestDistance = max(self.longestDistance, distance)
            longestCons(cur.left, cur, length)
            longestCons(cur.right, cur, length)

        longestCons(root, root, 0)
        return self.longestDistance
