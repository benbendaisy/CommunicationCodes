# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Given the root of a binary tree, flatten the tree into a "linked list":

        The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
        The "linked list" should be in the same order as a pre-order traversal of the binary tree.

        Example 1:

        Input: root = [1,2,5,3,4,null,6]
        Output: [1,null,2,null,3,null,4,null,5,null,6]
        Example 2:

        Input: root = []
        Output: []
        Example 3:

        Input: root = [0]
        Output: [0]

        Constraints:

        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100
    """
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        arr = []
        def preorderTraverse(node: TreeNode):
            if not node:
                return
            arr.append(node)
            preorderTraverse(node.left)
            preorderTraverse(node.right)

        preorderTraverse(root)
        n = len(arr)
        for idx in range(1, n):
            arr[idx - 1].left = None
            arr[idx - 1].right = arr[idx]
        arr[n - 1].left = None
        arr[n - 1].right = None

    def flatten2(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        arr = []
        while stack:
            node = stack.pop()
            arr.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        n = len(arr)
        for idx in range(1, n):
            arr[idx - 1].left = None
            arr[idx - 1].right = arr[idx]
        arr[n - 1].left = None
        arr[n - 1].right = None

    def flatten3(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        def flattenTree(node: TreeNode):
            if not node:
                return None

            # For a leaf node, we simply return the
            # node as is.
            if not node.left and not node.right:
                return node

            # Recursively flatten the left subtree
            leftTail = flattenTree(node.left)

            # Recursively flatten the right subtree
            rightTail = flattenTree(node.right)

            # If there was a left subtree, we shuffle the connections
            # around so that there is nothing on the left side
            # anymore.
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail

        flattenTree(root)
    
    def flatten4(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        arr = []
        def helper(node: TreeNode):
            if not node:
                return
            
            arr.append(node)
            helper(node.left)
            helper(node.right)
        helper(root)
        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]
        return root
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        arr = []
        def helper(node: TreeNode) -> TreeNode:
            if not node:
                return None
            if not node.left and not node.right:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            
            return right if right else left

        return helper(root)
