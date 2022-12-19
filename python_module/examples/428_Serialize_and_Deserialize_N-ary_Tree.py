"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class WrappableInt:
    def __init__(self, x):
        self.value = x
    def get_value(self):
        return self.value
    def increment(self):
        self.value += 1

class Codec:
    """
        Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
        Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
        For example, you may serialize the following 3-ary tree

        as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

        Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.

        For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

        You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

        Example 1:

        Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        Example 2:

        Input: root = [1,null,3,2,4,null,5,6]
        Output: [1,null,3,2,4,null,5,6]
        Example 3:

        Input: root = []
        Output: []
    """
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        def serialize_helper(node, serialized_list):
            if not node:
                return
            # Actual value
            serialized_list.append(chr(node.val + 48))
            # Number of children
            serialized_list.append(chr(len(node.children) + 48))

            for child in node.children:
                serialize_helper(child, serialized_list)
        serialize_list = []
        serialize_helper(root, serialize_list)
        return "".join(serialize_list)


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        def deserialize_helper(idx: WrappableInt):
            if idx.get_value() == len(data):
                return None
            node = Node(ord(data[idx.get_value()]) - 48, [])
            idx.increment()
            num_of_children = ord(data[idx.get_value()]) - 48

            for _ in range(num_of_children):
                idx.increment()
                node.children.append(deserialize_helper(idx))
            return node

        if not data:
            return None

        return deserialize_helper(WrappableInt(0))
