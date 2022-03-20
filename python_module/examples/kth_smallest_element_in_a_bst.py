# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if k <= 0:
            return -1
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1

if __name__ == "__main__":
    two = TreeNode(2, None, None)
    four = TreeNode(4, None, None)
    one = TreeNode(1, None, two)
    root = TreeNode(3, one, four)
    solution = Solution()
    ret = solution.kthSmallest(root, 1)
    print(ret)
