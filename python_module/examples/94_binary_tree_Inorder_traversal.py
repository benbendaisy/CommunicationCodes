from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        cur = root
        stack = []
        res = []
        while len(stack) > 0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res