# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def inorderTraverse(self, root: TreeNode):
        if not root:
            return
        self.inorderTraverse(root.left)
        self.arr.append(root.val)
        self.inorderTraverse(root.right)
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        self.inorderTraverse(root)
        return self.arr[k - 1]

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1
    
    def kthSmalles3(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        def helper(node: TreeNode):
            if not node:
                return
            
            helper(node.left)
            if len(self.heap) < k:
                heapq.heappush(self.heap, -node.val)
            elif len(self.heap) >= k and node.val < -self.heap[0]:
                heapq.heapop(self.heap)
                heaqp.heappush(self.heap, -node.val)
            helper(node.right)
        helper(root)
        return -self.heap[0] if self.heap else -1
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1
