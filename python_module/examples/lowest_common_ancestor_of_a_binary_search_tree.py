# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        cur = root
        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        cur = root
        parent_track = set()
        while cur and cur != p:
            parent_track.add(cur)
            if cur.val < p.val:
                cur = cur.right
            else:
                cur = cur.left
        parent_track.add(p)

        parents = {root: None}
        cur = root
        while cur and cur != q:
            if cur.val < q.val:
                parents[cur.right] = cur
                cur = cur.right
            else:
                parents[cur.left] = cur
                cur = cur.left

        cur = q
        while cur and cur not in parent_track:
            cur = parents[cur]
        return cur

    def searchTreeNode(self, root: 'TreeNode', s: 'TreeNode', set1):
        cur = root
        while cur and cur != s:
            set1.add(cur)
            cur = cur.left if cur.val > s.val else cur.right

if __name__ == "__main__":
    s = Solution()
    two = TreeNode(2)
    eight = TreeNode(8)
    six = TreeNode(6)
    six.left = two
    six.right = eight
    print(s.lowestCommonAncestor2(six, two, eight))