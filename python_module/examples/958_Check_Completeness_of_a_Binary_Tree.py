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
    Given the root of a binary tree, determine if it is a complete binary tree.

    In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Example 1:

    Input: root = [1,2,3,4,5,6]
    Output: true
    Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
    Example 2:

    Input: root = [1,2,3,4,5,null,7]
    Output: false
    Explanation: The node with value 7 isn't as far left as possible.
    """
    def isCompleteTree1(self, root: Optional[TreeNode]) -> bool:
        # Check if the root node is None, if so, return True (an empty tree is complete)
        if not root:
            return True

        # Create a deque to store the nodes of the tree in level order
        q = deque([root])

        # Traverse the tree in level order
        while q[0] is not None:
            # Remove the first node from the deque
            node = q.popleft()
            # Add the left and right child nodes of the current node to the deque
            q.append(node.left)
            q.append(node.right)
        # Remove any remaining None nodes from the beginning of the deque
        while q and q[0] is None:
            q.popleft()

        # Check if there are any remaining nodes in the deque
        # If so, the tree is not complete, so return False
        # Otherwise, the tree is complete, so return True
        return not bool(q)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        que = deque([root])
        see_null = False
        while que:
            node = que.popleft()
            if not node:
                see_null = True
                continue
            if see_null:
                return False
            que.append(node.left)
            que.append(node.right)

        return True
