# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec1:
    """
        Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

        Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

        Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

        Example 1:

        Input: root = [1,2,3,null,null,4,5]
        Output: [1,2,3,null,null,4,5]
        Example 2:

        Input: root = []
        Output: []

        Constraints:

        The number of nodes in the tree is in the range [0, 104].
        -1000 <= Node.val <= 1000
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        arr = []
        def serializeHelper(node: TreeNode):
            if not node:
                arr.append("#")
                return
            arr.append(node.val)
            serializeHelper(node.left)
            serializeHelper(node.right)

        serializeHelper(root)
        return " ".join(arr)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(" ")
        self.idx = 0
        def deserializeStr():
            if self.idx == len(arr) or arr[self.idx] == "#":
                return None
            node = TreeNode(arr[self.idx])
            self.idx += 1
            node.left = deserializeStr()
            self.idx += 1
            node.right = deserializeStr()
            return node

        return deserializeStr()

class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        arr = []
        while q:
            node = q.popleft()
            if not node:
                arr.append("#")
            else:
                arr.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return " ".join(arr)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(" ")
        root = TreeNode(arr[0])
        idx = 1
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if arr[idx] != "#":
                node.left = TreeNode(int(arr[idx]))
                q.append(node.left)
            idx += 1 # skip the left node
            if arr[idx] != "#":
                node.right = TreeNode(int(arr[idx]))
                q.append(node.right)
            idx += 1 # skip the right node
        return root

class Codec:
    """
        Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

        Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

        Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

        Example 1:

        Input: root = [1,2,3,null,null,4,5]
        Output: [1,2,3,null,null,4,5]
        Example 2:

        Input: root = []
        Output: []

        Constraints:

        The number of nodes in the tree is in the range [0, 104].
        -1000 <= Node.val <= 1000
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        arr = []
        def serializeHelper(node: TreeNode):
            if not node:
                arr.append("#")
                return
            arr.append(str(node.val))
            serializeHelper(node.left)
            serializeHelper(node.right)
            return " ".join(arr)

        return serializeHelper(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(" ")
        def deserializeStr():
            if not arr:
                return None
            elif arr[0] == "#":
                arr.pop(0)
                return None
            node = TreeNode(arr.pop(0))
            node.left = deserializeStr()
            node.right = deserializeStr()
            return node

        return deserializeStr()