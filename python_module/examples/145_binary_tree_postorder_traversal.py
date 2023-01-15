from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        cur = root
        res = []
        stack = [cur]
        visited = set()
        while stack:
            if stack[-1] in visited:
                cur = stack.pop()
                res.append(cur.val)
            else:
                cur = stack[-1]
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                visited.add(cur)
        return res
