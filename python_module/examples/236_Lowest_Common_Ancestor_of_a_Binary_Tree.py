# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

        Example 1:

        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3
        Explanation: The LCA of nodes 5 and 1 is 3.
        Example 2:

        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
        Example 3:

        Input: root = [1,2], p = 1, q = 2
        Output: 1

        Constraints:

        The number of nodes in the tree is in the range [2, 105].
        -109 <= Node.val <= 109
        All Node.val are unique.
        p != q
        p and q will exist in the tree.
    """
    def __init__(self):
        self.node = None
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursiveCommonAncestor(currNode: TreeNode):
            if not currNode:
                return False

            left = recursiveCommonAncestor(currNode.left)
            right = recursiveCommonAncestor(currNode.right)
            mid = p == currNode or q == currNode

            if left + right + mid >= 2:
                self.node = currNode

            return left or mid or right
        recursiveCommonAncestor(root)
        return self.node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        cur = root
        stack = deque([root])
        while p not in parents or q not in parents:
            cur = stack.pop()
            if cur.left:
                parents[cur.left] = cur
                stack.append(cur.left)

            if cur.right:
                parents[cur.right] = cur
                stack.append(cur.right)

        parentTrack = set()
        cur = p
        while cur:
            parentTrack.add(cur)
            cur = parents[cur]

        cur = q
        while cur not in parentTrack:
            cur = parents[cur]
        return cur