# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def countUnivalSubtrees1(self, root: Optional[TreeNode]) -> int:
        def countUnivalSubs(root: Optional[TreeNode]) -> bool:
            if not root.left and not root.right:
                self.cnt += 1
                return True

            isLeftUni = isRightUni = True
            if root.left:
                isLeftUni = countUnivalSubs(root.left) and root.left.val == root.val

            if root.right:
                isRightUni = countUnivalSubs(root.right) and root.right.val == root.val

            isUni = isLeftUni and isRightUni

            if not isUni:
                return False

            self.cnt += 1
            return isUni

        if not root:
            return 0
        countUnivalSubs(root)
        return self.cnt

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def countUnivalSubs(root: Optional[TreeNode], val: int) -> bool:
            if not root:
                return True

            if not all([countUnivalSubs(root.left, root.val), countUnivalSubs(root.right, root.val)]):
                return False

            self.cnt += 1
            return root.val == val

        countUnivalSubs(root, 0)
        return self.cnt