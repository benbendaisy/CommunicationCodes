# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator1:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.cur = 0
        def inOrderTraverse(root: TreeNode):
            if not root:
                return

            inOrderTraverse(root.left)
            self.arr.append(root.val)
            inOrderTraverse(root.right)
        inOrderTraverse(root)

    def next(self) -> int:
        res = self.arr[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return True if self.cur < len(self.arr) else False

class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.findLeftMostNodes(root)

    def findLeftMostNodes(self, root: TreeNode):
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        if not self.stack:
            return None
        cur = self.stack.pop()
        if cur.right:
            self.findLeftMostNodes(cur.right)
        return cur.val if cur else None

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BSTIterator3:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.idx = -1
        def helper(node: TreeNode):
            if not node:
                return
            helper(node.left)
            self.arr.append(node.val)
            helper(node.right)
        helper(root)
    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx]
    def hasNext(self) -> bool:
        return self.idx < len(self.arr) - 1

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.helper(root)
    def helper(self, node: TreeNode):
            cur = node
            while cur:
                self.stack.append(cur)
                cur = cur.left
        
    def next(self) -> int:
        if not self.stack:
            return None
        cur = self.stack.pop()
        self.helper(cur.right)
        return cur.val
    def hasNext(self) -> bool:
        return len(self.stack) > 0