# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.root = self.cur = TreeNode(val=0)
    def increasingBSTRecursive(self, root: TreeNode):
        if not root:
            return None

        self.increasingBSTRecursive(root.left)
        self.res.append(root)
        self.increasingBSTRecursive(root.right)

    def increasingBST1(self, root: TreeNode) -> TreeNode:
        self.increasingBSTRecursive(root)
        for i in range(1, len(self.res)):
            self.res[i - 1].left = None
            self.res[i - 1].right = self.res[i]
        self.res[-1].left = None
        self.res[-1].right = None

        return self.res[0]

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        res = []
        stack = []
        cur = root
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur)
            cur = cur.right

        for i in range(1, len(res)):
            res[i - 1].left = None
            res[i - 1].right = res[i]
        res[-1].left = None
        res[-1].right = None

        return res[0]

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def increasingBSTinner(node: TreeNode):
            if not node:
                return
            increasingBSTinner(node.left)
            self.cur.right = node
            node.left = None
            self.cur = node
            increasingBSTinner(node.right)
        increasingBSTinner(root)
        return self.root.right


