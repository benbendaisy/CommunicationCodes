# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
        Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

        Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

        The encoded string should be as compact as possible.

        Example 1:

        Input: root = [2,1,3]
        Output: [2,1,3]
        Example 2:

        Input: root = []
        Output: []
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        queue, data = collections.deque([root]), []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            data.append(str(node.val) if node else "#")
        return ",".join(data)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(",")
        data.reverse()
        root = TreeNode(data.pop())
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            l = data.pop()
            if l != "#":
                node.left = TreeNode(l)
                queue.append(node.left)
            r = data.pop()
            if r != "#":
                node.right = TreeNode(r)
                queue.append(node.right)
        return root