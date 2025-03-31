# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Given the root of a complete binary tree, return the number of the nodes in the tree.

        According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

        Design an algorithm that runs in less than O(n) time complexity.

        Example 1:

        Input: root = [1,2,3,4,5,6]
        Output: 6
        Example 2:

        Input: root = []
        Output: 0
        Example 3:

        Input: root = [1]
        Output: 1
    """
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        cnt = 0
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right
            cnt += 1
        return cnt
    
    def countNodes3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack, cur = [], root
        cnt = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right
            cnt += 1
        return cnt
    
    def countNodes4(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def compute_depth(node: TreeNode) -> int:
            """
            Return tree depth in O(d) time.
            """
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d
        
        def exists(idx: int, d: int, node: TreeNode) -> bool:
            """
            Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
            Return True if last level node idx exists. 
            Binary search with O(d) complexity.
            """
            left, right = 0, 2**d - 1
            for _ in range(d):
                pivot = left + (right - left) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        
        d = compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def compute_depth():
            dep = 0
            cur = root
            while cur.left:
                cur = cur.left
                dep += 1
            return dep
        
        def exists(idx: int, dep: int, node: TreeNode):
            left, right = 0, 2 ** dep - 1
            for _ in range(dep):
                pivot = (left + right) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        
        dep = compute_depth()
        if dep == 0:
            return 1
        
        left, right = 1, 2 ** dep - 1
        while left <= right:
            pivot = (left + right) // 2
            if exists(pivot, dep, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return (2 ** dep - 1) + left

