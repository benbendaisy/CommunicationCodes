# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

        Example 1:

        Input: root = [5,3,6,2,4,null,7], k = 9
        Output: true
        Example 2:

        Input: root = [5,3,6,2,4,null,7], k = 28
        Output: false

        Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -104 <= Node.val <= 104
        root is guaranteed to be a valid binary search tree.
        -105 <= k <= 105
    """
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorderTraverse(node: TreeNode):
            if not node:
                return
            inorderTraverse(node.left)
            arr.append(node.val)
            inorderTraverse(node.right)
        inorderTraverse(root)
        left, right = 0, len(arr) - 1
        while left < right:
            sums = arr[left] + arr[right]
            if sums == k:
                return True
            elif sums < k:
                left += 1
            else:
                right -= 1
        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashSet = set()
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node:
                if k - node.val in hashSet:
                    return True
                hashSet.add(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return False