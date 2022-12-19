from collections import deque
from typing import Optional
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

"""
# Definition for a binary tree node.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec1:
    """
    Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

    Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).

    For example, you may encode the following 3-ary tree to a binary tree in this way:

    Input: root = [1,null,3,2,4,null,5,6]
    Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

    Example 1:

    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,null,3,2,4,null,5,6]
    Example 2:

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Example 3:

    Input: root = []
    Output: []
    """
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        node = TreeNode(root.val)
        if len(root.children) > 0:
            node.left = self.encode(root.children[0])
        # the parent for the rest of the children
        cur = node.left
        # encode the rest of the children
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right

        return node



    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        root_node = Node(data.val, [])

        cur = data.left
        while cur:
            root_node.children.append(self.decode(cur))
            cur = cur.right
        return root_node

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None

        root_node = TreeNode(root.val)
        queue = deque([(root_node, root)])

        while queue:
            parent, cur = queue.popleft()
            prev_node, head_node = None, None
            # traverse each child one by one
            for child in cur.children:
                new_node = TreeNode(child.val)
                if prev_node:
                    prev_node.right = new_node
                else:
                    head_node = new_node
                prev_node = new_node
                queue.append((new_node, child))
            # use the first child in the left node of parent
            parent.left = head_node
        return root_node

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        # should set the default value to [] rather than None,
        # otherwise it wont pass the test cases.
        root_node = Node(data.val, [])
        queue = deque([(root_node, data)])
        while queue:
            parent, cur = queue.popleft()
            first_child = cur.left
            sibling = first_child

            while sibling:
                new_node = Node(sibling.val, [])
                parent.children.append(new_node)
                queue.append((new_node, sibling))
                sibling = sibling.right
        return root_node

