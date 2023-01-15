from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        def preorder_travel_recursive(node: TreeNode):
            if not node:
                return
            arr.append(node.val)
            preorder_travel_recursive(node.left)
            preorder_travel_recursive(node.right)
        preorder_travel_recursive(root)
        return arr


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        cur = root
        res = []
        stack = [cur]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res