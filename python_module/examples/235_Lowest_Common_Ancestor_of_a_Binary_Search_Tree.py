# Definition for a binary tree node.
from collections import deque
from functools import lru_cache


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

        Example 1:

        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6
        Explanation: The LCA of nodes 2 and 8 is 6.
        Example 2:

        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        Output: 2
        Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
        Example 3:

        Input: root = [2,1], p = 2, q = 1
        Output: 2

        Constraints:

        The number of nodes in the tree is in the range [2, 105].
        -109 <= Node.val <= 109
        All Node.val are unique.
        p != q
        p and q will exist in the BST.
    """
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = deque([root])
        while stack:
            cur = stack.pop()
            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)

            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)

        cur = p
        stackTrack = set()
        while cur:
            stackTrack.add(cur)
            cur = parent[cur]

        cur = q
        while cur and cur not in stackTrack:
            cur = parent[cur]

        return cur

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        @lru_cache(None)
        def dfs(node: TreeNode):
            if not node:
                return False

            leftNode = dfs(node.left)
            rightNode = dfs(node.right)
            mid = node == p or node == q
            if leftNode + rightNode + mid >= 2:
                self.node = node

            return leftNode or rightNode or mid

        dfs(root)
        return self.node

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur

        return cur

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        @lru_cache(None)
        def dfs(node):
            if not node:
                return None
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left)
            return node

        return dfs(root)
