# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.node = None
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursiveCommonAncestor(current_node):
            if not current_node:
                return False

            left = recursiveCommonAncestor(current_node.left)
            right = recursiveCommonAncestor(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right >= 2:
                self.node = current_node

            return left or right or mid
        recursiveCommonAncestor(root)
        return self.node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        cur = root
        stack = [root]
        while p not in parents or q not in parents:
            cur = stack.pop()
            if cur.left:
                parents[cur.left] = cur
                stack.append(cur.left)

            if cur.right:
                parents[cur.right] = cur
                stack.append(cur.right)

        parent_track = set()
        cur = p
        while cur:
            parent_track.add(cur)
            cur = parents[cur]
        cur = q
        while cur not in parent_track:
            cur = parents[cur]
        return cur